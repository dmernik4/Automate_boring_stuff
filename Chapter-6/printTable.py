# Prgram that prints the table!

tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dog", "cats", "moose", "goose"],
    ["Audi", "BMW", "Citroen", "Dodge"],
]


def print_table(table):
    # Create a list of 0's equal to number of inner list in table
    colWidth = [0] * len(tableData)

    # Find the longest word in each inner list and set the value to max length.
    maxLength = 0
    while maxLength < len(table):
        for item in table[maxLength]:
            if len(item) > colWidth[maxLength]:
                colWidth[maxLength] = len(item)
        maxLength += 1

    """Iterate through lists and taking every element from each list
    and printing it into a table, right justified according to the
    column width."""

    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(colWidth[item]), end=" ")
        print()


print_table(tableData)
