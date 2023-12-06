package validate_err

import (
	"errors"
	

	"github.com/go-playground/validator/v10"
)


type ErrorMessage struct{
	Field string `"json:field"`
	Message string `"json:message"`
}

var valerr validator.ValidationErrors

func GetErr(err error){
	if errors.As(err, &valerr){
		out := make([]ErrorMessage,len(valerr))
		for i, errmsg := range valerr{
			out[i] = ErrorMessage{errmsg.Field(),GetErrorMsg(errmsg)}
		}
	}
}

func GetErrorMsg(fe validator.FieldError)string{

	switch fe.Tag(){

		case "required":
			return "This field is required"

		case "min":
			return " The min value must be "+ fe.Param()
		
		case "max":
			return "The maximum value must be "+ fe.Param()
		case "let":
			return "Should be less than "+ fe.Param()

		case "startwith":
			return "Value must be start with "+fe.Param()

		case "endswith":
			return "Value must be end with "+fe.Param()
	}
	return "Unknown error"
}	

