package validate_err

import (
	"strings"
)

func GetField(rules string) string {

	for t := 0; t < len(rules); t++ {
		if string(rules[t]) == "." {
			return (string(rules[0:t]))
		} else {
			return "Unknown error ....get field function "
		}
	}

	return "Unknown"
}

func GetRule(rules string) string {
	for t := 0; t < len(rules); t++ {
		if string(rules[t]) == "." {
			return strings.SplitAfter(rules,".")[0]
		} else {
			return "Unknown .....get rule fuction "
		}
	}

	return "Unknown   ..... get rule not in for"
}
