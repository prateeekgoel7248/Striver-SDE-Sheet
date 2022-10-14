int longestSubSeg(vector<int> &arr , int n, int k){
    int zerocount=0;
    int ans=0;
    int i,j;
    for(i=0;i<n;i++){
        if(arr[i]==0){zerocount++;}        
        while(zerocount>k){
            if(arr[j]==0){  
                zerocount--;               
            }
            j++;
        }
        ans= max(ans, i-j+1);
    }
    return ans;
}
