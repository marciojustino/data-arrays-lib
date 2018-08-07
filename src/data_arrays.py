

class DataArrays():
    def sort(self, array):
        # remove all duplicate entries
        unique_list = self.remove_duplicates(array)

        smaller = biggest = 0
        for i in range(len(unique_list)):
            smaller = unique_list[i]
            j = i
            while j < len(unique_list):
                if unique_list[j] < unique_list[i]:
                    smaller = unique_list[j]
                    biggest = unique_list[i]
                    unique_list[i] = smaller
                    unique_list[j] = biggest
                j += 1
        return unique_list

    def remove_duplicates(self, array):
        unique_list = []
        for i in array:
            if i not in unique_list:
                unique_list.append(i)
        return unique_list
