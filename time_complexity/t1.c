 int j = 0;
        for(int i = 0; i < n; ++i) {
            while(j < n && arr[i] < arr[j]) {
                j++;
            }
        }

//O(n) as inner loop runs only once as j isn't reset to 0