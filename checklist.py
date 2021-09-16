import os

checklist = list()

# Class of colors first used to better reference color titles
class bcolors:
  PURPLEHEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  YELLOWWARNING = '\033[93m'
  FAILRED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  ENDCNORMAL = '\033[0m'

# List of colors used for rainbow checklist effect
colors = [
  '\033[95m',
  '\033[94m',
  '\033[96m',
  '\033[92m',
  '\033[93m',
  '\033[91m',
  '\033[0m',
]

""" CRUD OPERATIONS: """
def create(item):
  checklist.append(item)

def read(index):
  if index > len(checklist): print(f"{bcolors.YELLOWWARNING}Index doesn't exist in checklist.{bcolors.ENDCNORMAL}")
  else: return f"--> {bcolors.OKCYAN}{checklist[index]}{bcolors.ENDCNORMAL}"

def update(index, item):
  checklist[index] = item

def destroy(index):
  if index > len(checklist): print(f"{bcolors.YELLOWWARNING}Index doesn't exist in checklist.{bcolors.ENDCNORMAL}")
  else: checklist.pop(index)

def list_all_items():
  print("======= ALL ITEMS: =======")
  for i in range(len(checklist)):
    # Print rainbow checklist using list of colors:
    print(f"{colors[i % (len(colors) - 1)]}{str(i)} {checklist[i]}{colors[len(colors) - 1]}")
  print("==========================")

def checkmark_item(index):
  # Toggle '√' if it exists, else add it
  if checklist[index][0] == "√":
    checklist[index] = checklist[index][2:len(checklist[index])]
  else:
    checklist[index] = "√ " + checklist[index]

""" The user inputs """
def select(function_code):
  if function_code == "C":
    # Add a new item to end of list
    input_item = input("What item do you want to add? ")
    create(input_item)
  elif function_code == "R":
    # Read an item from given index
    item_index = int(input("Which index number do you want to read? "))
    print(read(item_index))
  elif function_code == "U":
    # Update an item at certain index with error checking
    item_index = int(input("Which index to update? "))
    if item_index > len(checklist): print("Index doesn't exist in checklist.")
    else: 
      input_item = input("What do you want to replace it with? ")
      update(item_index, input_item)
  elif function_code == "M":
    # Mark an item as completed at certain index
    item_index = int(input("Which index number do you want to mark as completed? "))
    checkmark_item(item_index)
  elif function_code == "D":
    # Delete an item at certain index
    item_index = int(input("Which index to delete? "))
    destroy(item_index)
  elif function_code == "P":
    # print all items
    list_all_items()
  elif function_code == "Q":
    # Quit. Where our loop will stop.
    return False
  else:
    # Catch all
    print("\n* Unknown Option! *\n")
  return True

def user_input(prompt):
  user_input = input(prompt)
  return user_input


""" TESTS """
def test():
  create("purple sox")
  create("orange sox")
  create("haircut")
  create("mailbox")
  create("pick up laundry")
  create("purple sox")
  create("orange sox")
  create("haircut")
  create("mailbox")
  create("pick up laundry")
  create("purple sox")
  create("orange sox")
  create("haircut")
  create("mailbox")
  create("pick up laundry")

  # print(read(1))

  # update(1, "green tea")
  # print(checklist)
  # destroy(0)

  # print(checklist)

  # list_all_items()

  # select("C")
  # list_all_items()
  # select("R")

  # user_value = user_input("please enter value: ")
  # print(user_value)

test()



""" RUN THE APPLICATION """
running = True
while running:
  selection = user_input(
    f"{bcolors.OKBLUE}Press C to Add to list, {bcolors.PURPLEHEADER}\nR to Read from list, {bcolors.OKBLUE}\nU to Update an item, {bcolors.OKGREEN}\nM to Checkmark Toggle an item, {bcolors.FAILRED}\nD to Delete an item, {bcolors.PURPLEHEADER}\nP to Display list, {bcolors.YELLOWWARNING}\nand Q to quit:\n{bcolors.ENDCNORMAL}")
  os.system('clear')
  running = select(selection.upper())
