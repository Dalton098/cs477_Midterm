import xlsxwriter
import pandas as pd 
import argparse

def main(log, batch, lr, func):

   run_log_sheet = pd.ExcelFile('run_log_sheet.xlsx')
   writer = pd.ExcelWriter('run_log_sheet.xlsx', engine='xlsxwriter')
   sheets = run_log_sheet.sheet_names
   
   acc = ''
   log = open(log)
   for line in log:
       if 'Test accuracy' in line:
          acc = line.split(':')[1]
          
   new_func_row = pd.DataFrame({'Learning Rate': [lr], 'Batch Size': [batch], 'Accuracy': [acc]})
  
   if func not in sheets: 
      new_func_row.to_excel(writer, sheet_name=func)
   else: 
      func_sheet = pd.read_excel(run_log_sheet, func)
      func_sheet = func_sheet.concat(new_func_row)
      func_sheet.to_excel(writer, sheet_name=func)
       
 
if __name__ == '__main__':
   parser = argparse.ArgumentParser(description= 'Format output to Spreadsheet')
   parser.add_argument('--log', help='A log file from a run')
   parser.add_argument('--batch', help = 'batch size')
   parser.add_argument('--lr', help = 'learning rate')
   parser.add_argument('--func', help = 'activation function')
   args = parser.parse_args()
   main(log=args.log, batch=args.batch, lr=args.lr, func=args.func)
