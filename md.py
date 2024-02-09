import markdownify
import sys
import argparse
from pathlib import Path

def main(argv=sys.argv[1:]):
   parser = argparse.ArgumentParser(description='Convert an html file to markdown.')
   parser.add_argument('-i', '--input',  required=False, default=sys.stdin,  type=argparse.FileType('r'), help='The html file name to be converted')
   parser.add_argument('-o', '--output', required=False, default=sys.stdout, type=str, help='The markdown file name to be written')

   args = parser.parse_args(argv)
   html_text = args.input.read()
   args.input.close()

   # Use markdownify() function to convert HTML to Markdown
   markdown_text = markdownify.markdownify(html_text)

   if args.output:
      # if output file has a slash
      last_slash_index = args.output.rfind('/')
      if last_slash_index > 0:
         # we should create the folder of the output file
         folder_name = args.output[0:last_slash_index]
         # create the folder
         Path(folder_name).mkdir(parents=True, exist_ok=True)
      # write to file
      output_file = open(args.output, "w")
      output_file.write(markdown_text)
      output_file.close()
   else:
      print(markdown_text)

if __name__ == '__main__':
    main()
