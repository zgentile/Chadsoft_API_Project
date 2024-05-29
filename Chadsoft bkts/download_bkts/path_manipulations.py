''' This function finds the rightmost occurrence of a quotation mark, and takes
all content that follows that. This is handy because of the way that I am splitting
the extracted information for each leaderboard. It turns out that after running some
manipulations, the path for each ghost file comes directly after the final quotation 
mark every time. '''
def extract_path(long_string):
  # Find the last occurrence of the quotation mark
  last_quote_index = long_string.rfind('"')

  if last_quote_index != -1:
      ending_part = long_string[last_quote_index + 1:]
      return ending_part
  else:
      print("No quotation mark found in the string.")

''' This function takes the rightmost level of a given path.
The rkg files will be named using this function when downloaded. '''
def adjust_path(path):
  # Find the last occurrence of a forward slash
  last_slash_index = path.rfind("/")

  if last_slash_index != -1:
    return path[last_slash_index + 1:]
  else:
    return path