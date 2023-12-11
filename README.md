#  VEC validation error customization 

Gin (Golang) validation error package for easy request validation by Saparov

#  Installing
Install from repository
<pre>
<code>go get github.com/Kesha005/validate_err</code>
</pre>

#  Usage

Repository is not validation package, it's for customization for validation error Gin framework

To use custom messages only we should create map with field and that's field errors
<h4>Example:</h4>
<pre>
  <code>
    
    package handlers
  
    import (
	        "net/http"  
	        "github.com/gin-gonic/gin"
	        "gorm.io/gorm"
	        "github.com/Kesha005/validate_err")


    type BookRequest struct{
	      Name string `json:"name" binding:"required"`
	      Author string `json:"author"`
    }

    var validation_err = map[string]string{
	      "name.required" :"Name field is required",
	      "author.required":"Author field is required",
    }

    func (db datab) Store(ctx *gin.Context){
	      body := BookRequest{}
	      if  err := ctx.ShouldBindJSON(&body);err!=nil{
		    data := validate_err.GetErr(err,&validation_err)
		    ctx.AbortWithStatusJSON(http.StatusBadRequest, gin.H{"errors": data})
		    return 
	    }
	    var book models.Book

	    book.Name = body.Name
	    book.Author = body.Author

	    if res := db.Db.Create(&book);res.Error!=nil{
		  ctx.AbortWithError(http.StatusForbidden,res.Error)
		  return 
  	  }
	    ctx.JSON(http.StatusAccepted,&book)
	
    }
    
  </code>
</pre>

