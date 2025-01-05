

def reward(childrensIDs, chocolates, childID, extra_chocolates ):    


    #find the index of the child exists in the list
    if childID not in childrensIDs:
        print("Error: child is invalid")
        return 1

    # find the index of the child in the list
    child_index=childrensIDs.index(childID)

    # Add extra chocolates to child current chocolates
    chocolates[child_index] += extra_chocolates

    # Calculate the total chocolates received by all childern
    total_chocolates = sum(chocolates)

    #display the total chocolates recieved by all children
    print(f"\nUpdated list of chocolates: {chocolates}")
    print(f"\nTotal chocolates received by all children: {total_chocolates}")


