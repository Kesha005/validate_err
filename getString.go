package validate_err

import "fmt"

func GetField(rules string) string {

	for t := 0; t < len(rules); t++ {
		if string(rules[t]) == "." {
			return (string(rules[0:t]))
		} else {
			return "Unknown"
		}
	}

	return "Unknown"
}

func GetRule(rules string) string {
	for t := 0; t < len(rules); t++ {
		if string(rules[t]) == "." {
			return (string(rules[t+1:]))
		} else {
			return "Unknown"
		}
	}

	return "Unknown"
}
