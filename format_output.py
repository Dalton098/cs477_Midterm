import xlsxwriter
import pandas as pd 
import argparse

def main(relu_log, batch, lr):

   run_log_sheet = pd.ExcelFile('run_log_sheet.xlsx')
   writer = pd.ExcelWriter('run_log_sheet.xlsx', engine='xlsxwriter')
   
   functions = ['relu']
   for func in functions:
       sheets = run_log_sheet.sheet_names
       #acc = ''
      # if func == 'leaky':
       #   print('leaky')
      #    log = leaky_log
     #  elif func == 'softmax':
     #     print('softmax')
     #     log = softmax_log
     #  elif func == 'relu':
     #     print('relu')
     #     log = relu_log

       log = open(str(relu_log))
       for line in log:
           print('open')
           if 'Test accuracy' in line:
              print('Here')
              acc = line.split(':')[1]
          
       new_func_row = pd.DataFrame({'Learning Rate': [lr], 'Batch Size': [batch], 'Accuracy': [acc]})
  
       if func not in sheets: 
          new_func_row.to_excel(writer, sheet_name=func)
       else: 
          func_sheet = pd.read_excel(run_log_sheet, func)
          func_sheet = pd.concat([new_func_row, func_sheet]) #.reset_index(drop=True)
          func_sheet.to_excel(writer, sheet_name=func)
   writer.save()       
 
if __name__ == '__main__':
   parser = argparse.ArgumentParser(description= 'Format output to Spreadsheet')
   #parser.add_argument('--leaky_log', help='A log file from a run')
   #parser.add_argument('--softmax_log', help='A log file from  a run')
   parser.add_argument('--relu_log', help='A log file from a run')
   parser.add_argument('--batch', help = 'batch size')
   parser.add_argument('--lr', help = 'learning rate')
   #parser.add_argument('--func', help = 'activation function')
   args = parser.parse_args()
   main(relu_log=args.relu_log, batch=args.batch, lr=args.lr) #, func=args.func)
