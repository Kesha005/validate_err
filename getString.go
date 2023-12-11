package validate_err

import (
	"strings"
)

func GetField(rules string) string {

	for t := 0; t < len(rules); t++ {
		if string(rules[t]) == "." {
			return (string(rules[0:t]))
		} 
	}

	return "Unknown"
}
//Code will be modifed there
func GetRule(rules string) string {
	for t := 0; t < len(rules); t++ {
		if string(rules[t]) == "." {
			return strings.SplitAfter(rules,".")[1]
		} 
	}

	return "Unknown   ..... get rule not in for"
}
