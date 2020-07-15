function start_file_upload() {
    document.getElementById('fileid').click();
}

function on_file_selected(event) {
    var reader = new FileReader();
    var result = [];

    reader.onload = function (evt) {

        lines = evt.target.result.split(/\r?\n/);

        lines.forEach(function (line) {
            result.push(line);
        });
    };
    reader.onloadend = function () {
        generateXML(result);
    };
    reader.readAsText(event.target.files[0]);
}

function generateXML(inp_arr) {

    var options = {
        scriptPath: path.join(__dirname, '/engine'),
        args: inp_arr
    }

    pythonShell.PythonShell.run('batch_operation.py', options, function (error, result) {
        var jsonResult = JSON.parse(result[0])
        if (jsonResult['code']) {
            window.location = 'genTestCases.xls';
        }
    })
}