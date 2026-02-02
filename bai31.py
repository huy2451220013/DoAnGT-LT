class Solution(object):
    def duplicateZeros(self, arr):
        st = []
        for i in range(len(arr)):
            if len(st)<len(arr):
                if arr[i]==0:
                    st.append(arr[i])
                    st.append(0)
                else:
                    st.append(arr[i])
        for i in range(len(arr)):
            arr[i]=st[i]