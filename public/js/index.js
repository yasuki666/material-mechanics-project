/*ocument.addEventListener('DOMContentLoaded', function(event){
    var find_introdiction = document.getElementById('introduction');
    fso = new ActiveXObject("Scripting.FileSystemObject");
    ts = fso.OpenTextFile("text,txt",ForReading);
    s = ts.ReadLine;
    find_introdiction.innerHTML = s;


})
*/

var ReadText = function(){
    var file=document.getElementById("file").files[0];
    var reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function(data){
        document.getElementById('introduction').innerHTML = this.result;
    };
}