function init() {

const inpFile = document.getElementById("inpFile")
  const btnUpload = document.getElementById("btnUpload")

  btnUpload.addEventListener("click", function () {
      const formData = new FormData();    //special javascript object for holding form-data to eventually submit to web-server

      console.log(inpFile.files);
      for (const file of inpFile.files){
          formData.append("myFiles[]", file);  // the name "myFiles" represents all files to submit
      }

/*----------------------------------------------------------------------------------------------------
PHP likes the format of "myFiles[]" using square brackets when submitting multiple files, so the sqaure
brackets must be included - but other web-servers such as node.js are fine with just "myFiles" without
the square brackets. 
------------------------------------------------------------------------------------------------------*/

//note that using 'myFiles' in the line above is similar to putting into the input type - name="myFiles"
  /*    
      for (const [key, value] of formData) {
          console.log(`key: ${key}`);
          console.log(`value: ${value}`);
      }
  */ 
      fetch('http://localhost:3000/upload', {
          method: "post",
          body: formData
      }).catch(console.error);

/*--------------------------------------------------------------------------------------------------------
By submitting the 'body' as 'formData' the Javascript knows that it's a formData object, as used in 
<formData.append("myFiles", file);> above. 
----------------------------------------------------------------------------------------------------------*/

  });
  
}

window.onload = init;
