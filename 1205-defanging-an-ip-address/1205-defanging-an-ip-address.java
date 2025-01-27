class Solution {
public String defangIPaddr(String address) {
int index = address.indexOf(".");
for(int i = 0; i<3; i++){
address = address.substring(0,index) + "[" + address.substring(index,index+1) + "]" + address.substring(index+1);
index = address.substring(0,index+2).length() + address.substring(index+2).indexOf(".");
}
return address;
}}