class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<String>();
 
    //stack.push(path.substring(0,1));
 
    while(path.length()> 0 && path.charAt(path.length()-1) =='/'){
        path = path.substring(0, path.length()-1);
    }
 
    int start = 0;
    for(int i=1; i<path.length(); i++){
        if(path.charAt(i) == '/'){
            stack.push(path.substring(start, i));
            start = i;
        }else if(i==path.length()-1){
            stack.push(path.substring(start));
        }
    }
 
    LinkedList<String> result = new LinkedList<String>();
    int back = 0;
    while(!stack.isEmpty()){
        String top = stack.pop();
 
        if(top.equals("/.") || top.equals("/")){
            //nothing
        }else if(top.equals("/..")){
            back++;
        }else{
            if(back > 0){
                back--;
            }else{
                result.push(top);
            }
        }
    }
 
    //if empty, return "/"
    if(result.isEmpty()){
        return "/";
    }
 
    StringBuilder sb = new StringBuilder();
    while(!result.isEmpty()){
        String s = result.pop();
        sb.append(s);
    }
 
    return sb.toString();
    }
}