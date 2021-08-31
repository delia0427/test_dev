var caseTreeInit = function() {
    var zTreeObj;

var setting = {
        view: {
            addHoverDom: false,
            removeHoverDom: false,
            selectedMulti: false
        },
        check: {
            enable: true
        },
        data: {
            simpleData: {
                enable: true
            }
        },
        edit: {
            enable: true
        }
    };

var zNodes =[
//                {id:4, pId:0, name:"大数据量 演示", open:false},
//                {id:401, pId:4, name:"一次性加载大数据量"},
//                {id:40101, pId:401, name:"123分批异步加载大数据量"},
            ];
$(document).ready(function(){

   $.get("/task/get_case_tree",
   function(resp,status){
   var zNodes = resp.data;
   zTreeObj = $.fn.zTree.init($("#treeDemo"), setting, zNodes);   // 默认自动执行
   zTreeObj.expandAll(false);   // 全部展开（true）/折叠（false）
   })
});
}




