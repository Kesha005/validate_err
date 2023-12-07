package main

import "fmt"



func main(){
	
	rule := map[string]string{
		"name.required":"The name must be required",
	}
	for i,r := range rule{
		
		fmt.Println(i+" "+r)
		for t:=0; t<len(i);t++{
			if string(i[t])=="."{
				
				fmt.Println("There is have")
				fmt.Println(string(i[0:t]))
			}else{
				fmt.Println("There is not")
			}
		} 
	}
}