let regex = /.*csrftoken=([^;.]*).*$/ ;
var xCSRFToken = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]

// 清理下拉选项
function clearOption(cmb) {
    for (let i = 0;i <= cmb.length + 1; i++){
        cmb.options.remove(cmb[i])
    }
}

// 创建下拉选项
function cmbAddOption(cmb, obj) {
    let option = document.createElement("option");
    cmb.options.add(option);
    option.innerHTML = obj.name;
    option.value = obj.id;
}


// 获取项目列表
var ProjectInit = function(_cmbProject) {
    var cmbProject = document.getElementById(_cmbProject);



    function getProjectListInfo() {
        // 获取项目列表信息
        $.get("/project/project_list", {}, function(resp){
            if (resp.status === 10200) {
                let dataList = resp.data;
                for (let i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbProject, dataList[i]);
                };
//                let cases = resp.data;
//                for (let i = 0; i < cases.length; i++) {
//                    let option = '<input type="checkbox" name="' + cases[i].name + '" value="' + cases[i].id + '" /> '
//                    + cases[i].name;
//                    options = options + option;
//                }
//                let devCaseList = document.querySelector(".caseList");
//                devCaseList.innerHTML = options;
            } else {
                window.alert(resp.message);
                }
        });
    }

    // 调用getProjectListInfo函数
    getProjectListInfo();
}

// 获取某一个项目的模块列表
var ModuleInit = function(_cmbModule, pid ){
    var cmbModule = document.getElementById(_cmbModule);
//    let regex = /.*csrftoken=([^;.]*).*$/ ;
//    var xCSRFToken = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1]


    function getModuleListInfo() {
        // 获取模块列表信息
        $.post("/module/module_list",
        {"pid":pid,
        csrfmiddlewaretoken: xCSRFToken},
        function(resp){
            if (resp.status === 10200) {
                let dataList = resp.data;
                for (let i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbModule, dataList[i]);
                };
            } else {
                window.alert(resp.message);
                }
        });
    }

    clearOption(cmbModule);
    // 调用getModuleListInfo函数
    getModuleListInfo();
}



// 获取用例信息
var TestCaseInit = function() {
    var url = document.location;   // 获取url
    var cid = url.pathname.split("/")[3];  // 从url获取用例idvalue

    $.post("/case/get_case_info",
        {
            cid: cid,
            csrfmiddlewaretoken: xCSRFToken

        },
        function(resp,status){
        document.querySelector("#req_url").value = resp.result.url;   // 重写进入结果框
        document.querySelector('input[value='+resp.result.method+']').setAttribute("checked", "");
        document.querySelector("#header").value = resp.result.header;   // 重写进入结果框
        document.querySelector('input[value='+resp.result.parameter_type+']').setAttribute("checked", "");
        document.querySelector("#parameter").value = resp.result.parameter;   // 重写进入结果框
        document.querySelector("#result").value = resp.result.result_body;   // 重写进入结果框
        document.querySelector('input[value='+resp.result.aesert_type+']').setAttribute("checked", "");
        document.querySelector("#assert").value = resp.result.result_body;   // 重写进入结果框
        document.querySelector("#assert_result").value = resp.result.assert_text;   // 重写进入结果框
        document.querySelector("#case_name").value = resp.result.name;   // 重写进入结果框

        SelectInit(resp.result.project_id, resp.result.module_id);
        })
}


// 初始化“项目>模块” 二级联动菜单
var SelectInit = function(defaultProjectId, defaultModuleId) {
    var cmbProject = document.getElementById("selectProject");
    var cmbModule = document.getElementById("selectModule");
    var dataList = [];
    console.log("qqqqq", cmbProject);

    // 设置默认选项
    function setDefaultOption(obj, id) {
        for (var i = 0; i < obj.options.length; i++) {
            if (obj[i].value == id) {
                obj.selectedIndex = i;
            return;}
        }
    }

    // 创建下拉选项
    function addOption(cmb, obj) {
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = obj.name;
        option.value = obj.id;
    }

    // 改变项目
    function changeProject() {
        cmbModule.options.length = 0;
        if (cmbProject.selectedIndex == -1) {
            return;
        }
        var pid = cmbProject.options[cmbProject.selectedIndex].value;
        console.log("pid:",  pid, dataList.length)
        for (let i=0 ; i < dataList.length; i++) {
            console.log("pdataList[i].id", dataList[i] ,dataList[i].id);
            if (dataList[i].id == pid) {
                let modules = dataList[i].module_list;
                console.log("modulessssssssss",  modules);
                for (let j = 0; j < modules.length; j++) {
                    console.log("cmbModuleaaaaa", cmbModule);
                    addOption(cmbModule, modules[j]);
                }
            }
        }
    }

    function getSelectData() {
        // 调用获取select 数据列表
        $.get("/case/get_select_data", {}, function ( resp) {
            if (resp.status === 10200) {
                dataList = resp.data;
                // 遍历项目
                for (var i = 0; i < dataList.length; i++) {
                    addOption(cmbProject, dataList[i]);


                }

                setDefaultOption(cmbProject, defaultProjectId);
                changeProject();
                cmbProject.onchange = changeProject;
            }
            setDefaultOption(cmbModule, defaultModuleId)
        });
    }

    getSelectData();




}