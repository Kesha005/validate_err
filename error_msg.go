package validate_err

import (
	"errors"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
)


type ErrorMessage struct{
	Field string `"json:field"`
	Message string `"json:message"`
}

var valerr validator.ValidationErrors

func GetErr(err error, rule *map[string]string)[]ErrorMessage{
	if errors.As(err, &valerr){
		out := make([]ErrorMessage,len(valerr))
		for i, errmsg := range valerr{
			out[i] = ErrorMessage{strings.ToLower(errmsg.Field()),GetErrorMsg(errmsg, rule)}
		}
		return out
	}
	return nil
	
}


var validation_err = map[string]string{
	"name.required" :"Name field is required",
	"author.required":"Author field is required",
}

func GetErrorMsg(fe validator.FieldError, rule *map[string]string)string{
	
}
