

jQuery(document).ready(function(){ 

    $("#category").jqGrid({                                       
    url:'display/',
    datatype:'json',
    datatype: 'local',
    width: 500, //specify width; optional
    colNames:['Α/Α','Κατηγορία'], //define column names
    colModel:[
    {name:'id', index:'id', key: true, width:30},
    {name:'name', index:'name', width:100,align:'center',editable:true,editoptions:{size:40},editrules:{required:true}}
    ], //define column models
    rowNum:10,
    rowList:[10,20,30],
    pager: '#pagernav', 
    sortname: 'id',         
    viewrecords: true,   //if true, displays the total number of records, etc. as: "View X to Y out of Z” optional
    sortorder: "asc",           //sort order; optional
    caption:"Κατηγορίες απογραφής",
    editurl:'edit/',
    height:'100%',
    width: '100%'
    });
    
jQuery("#category").jqGrid('navGrid','#pagernav',
{search:true,add:true,edit:true,del:true},                              //options
{width:400,height:430,reloadAfterSubmit:true,closeAfterEdit: true},    // edit options
{width:400,height:430,reloadAfterSubmit:true,closeAfterAdd: true},    // add options
{width:270,reloadAfterSubmit:true},                                   // del options
{}                                                                   // search options
);
    
});
