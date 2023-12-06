package validate_err

import (
	"errors"
	"fmt"
	"net/http"

	"github.com/go-playground/validator/v10"
)


type ErrorMessage struct{
	Field string `"json:field"`
	Message string `"json:message"`
}

func GetErrorMsg(fe validator.FieldError)string{

	switch fe.Tag(){
		case "required":
			return ""
		case "min":
			return ""
	}
	return "Unknown error"
}	