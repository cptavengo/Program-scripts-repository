#!/usr/bin/env python3

def string_cleanup(string):
  string = string.lower() #conver input to lowercase
  new_string = "" #define new empty string for iteration
  for letter in string:
    if letter.isalpha() == True or letter == " ": #check if letter is a space or is part of the alphabet only, no numbers
      new_string += letter #add letter if check passed to new_string

  return new_string

def dict_cleanup(object):
  string = object.lower() #convert input to lowercase
  new_string = "" #define new empty string for iteration
  for letter in string:
    if letter.isalpha() == True or letter == " ": #check if letter is a space or is part of the alphabet only, no numbers
      new_string += letter #add letter if check passed to new_string
  new_list = new_string.split()
  new_dict = {}
  new_dict_values_list = []
  uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how" \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
  for item in new_list:
    if item not in new_dict.keys():
      new_dict[item] = 1
    elif item in new_dict.keys():
      new_dict[item] += 1
  for key in new_dict.copy():
    if key in uninteresting_words:
      del new_dict[key]
  for value in new_dict.values():
    new_dict_values_list.append(value)

  return new_dict_values
