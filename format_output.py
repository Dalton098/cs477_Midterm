import xlsxwriter
import pandas as pd 
import argparse

def main(leaky_log, softmax_log, relu_log, batch, lr):

   run_log_sheet = pd.ExcelFile('run_log_sheet.xlsx')
   writer = pd.ExcelWriter('run_log_sheet.xlsx', engine='xlsxwriter')
   sheets = run_log_sheet.sheet_names
   
   functions = ['leaky', 'softmax', 'relu']
   for func in functions:
       acc = ''
       if func == 'leaky':
          log = leaky_log
       elif func == 'softmax':
          log = softmax_log
       elif func == 'relu':
          log = relu_log

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
   parser.add_argument('--leaky_log', help='A log file from a run')
   parser.add_argument('--softmax_log', help='A log file from  a run')
   parser.add_argument('--relu_log', help='A log file from a run')
   parser.add_argument('--batch', help = 'batch size')
   parser.add_argument('--lr', help = 'learning rate')
   #parser.add_argument('--func', help = 'activation function')
   args = parser.parse_args()
   main(leaky_log=args.leaky_log, softmax_log=args.softmax_log, relu_log=args.relu_log, batch=args.batch, lr=args.lr) #, func=args.func)
