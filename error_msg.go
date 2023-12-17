package validate_err

import (
	"errors"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
)

/*
	Error message struct
	returns error field and message that field
*/
type ErrorMessage struct{
	Field string `json:"field"`
	Message string `json:"message"`
}

var valerr validator.ValidationErrors



func GetErr(err error, rule *map[string]string)gin.HandlerFunc{

	return func (c *gin.Context) {
		err := c.ShouldBindJSON("some Json validation struct")
		if err!=nil{
			
		}
	}
	// if errors.As(err, &valerr){
	// 	out := make([]ErrorMessage,len(valerr))
	// 	for i, errmsg := range valerr{
	// 		out[i] = ErrorMessage{strings.ToLower(errmsg.Field()),GetErrorMsg(errmsg, rule)}
	// 	}
	// 	return gin.H{"errors":out}
	// }
	// return nil
	
}


// var validation_err = map[string]string{
// 	"name.required" :"Name field is required",
// 	"author.required":"Author field is required",
// }

func GetErrorMsg(fe validator.FieldError, rule *map[string]string)string{
	for i ,msg := range *rule{
		if strings.ToLower(fe.Field()) == GetField(i) && fe.Tag()==GetRule(i){
			return msg
		}else{
			return "Unknown error"
		}
	}
	return "Unknown error"
}
