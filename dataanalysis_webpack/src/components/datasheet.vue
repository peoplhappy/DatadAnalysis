<template>
  <div>
    <el-dialog title="文件上传" :visible.sync="dialogVisible" width="60%" @close="closeDialog">
      <span>
        <el-radio-group v-model="radio" @change="changeradio">
          <el-radio label="1">csv</el-radio>
          <el-radio label="2">xlsx or xls</el-radio>
        </el-radio-group>
      </span>
      <el-upload
        align="center"
        class="upload-demo"
        drag
        action="http://localhost:5000/file/uploader"
        multiple
        :before-upload="handleBefore"
        :data="filepostdata"
        :on-success="afterupload"
        v-if="show"
        ref="tab"
      >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text" align="left">
          将文件拖到此处，或
          <em>点击上传</em>
        </div>
        <div class="el-upload__tip" slot="tip">只能上传xlsx,txt,csv文件</div>
      </el-upload>
      <span v-if="flag!=undefined">
        <el-checkbox-group v-model="csvcheckList" v-if="flag" @change="changcheckbox">
          <el-checkbox label="1">
            <el-input v-model="csvFormdata.headerstart" placeholder="请输入第几行" size="mini">
                 <template slot="prepend">从第几行开始读取</template>
            </el-input>
          </el-checkbox>
          <el-checkbox label="2">
            <el-input v-model="csvFormdata.sep" placeholder="请输入分隔符" size="mini">
              <template slot="prepend">分隔符(默认为,)</template>
            </el-input>
          </el-checkbox>
          <el-checkbox label="3">分隔符为空白字符</el-checkbox>
          <el-checkbox label="4">
            <el-input v-model="csvFormdata.colunms" placeholder="请输入表格头" size="mini">
                <template slot="prepend">表格头(以,隔开)</template>
            </el-input>
          </el-checkbox>
          <el-checkbox label="5">
            <el-input v-model="csvFormdata.dfindex" placeholder="请输入索引列" size="mini">
                <template slot="prepend">指定索引列</template>
            </el-input>
          </el-checkbox>
        </el-checkbox-group>
        <el-checkbox-group v-model="excelcheckList" v-if="!flag">
          <el-checkbox label="要读取的sheet名称或索引">
            <el-input v-model="excelFormdata.sheetname" placeholder="请输入sheet名称或索引" size="mini"></el-input>
          </el-checkbox>
          <el-checkbox label="从第几行开始读取">
            <el-input v-model="excelFormdata.headerstart" placeholder="请输入第几行" size="mini"></el-input>
          </el-checkbox>
          <el-checkbox label="表格头(以,隔开)">
            <el-input v-model="excelFormdata.colunms" placeholder="请输入表格头" size="mini"></el-input>
          </el-checkbox>
          <el-checkbox label="指定索引列">
            <el-input v-model="excelFormdata.dfindex" placeholder="请输入索引列" size="mini"></el-input>
          </el-checkbox>
        </el-checkbox-group>
      </span>
    </el-dialog>
    <el-button @click="dialogVisible = true">上传文件</el-button>
    <el-table :data="tableData" style="width: 100%" v-if="!show" border>
      <el-table-column v-for="(item, index) in tablecolumn" :key="index" :label="item">
        <template slot-scope="scope">
          <span>{{scope.row[index]}}</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "datasheet",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      show: true,
      tableData: [],
      filepostdata: {},
      tablecolumn: [],
      dialogVisible: false,
      checkList: [],
      radio: "0",
      flag: null,
      csvFormdata: {
        headerstart: null,
        sep: ",",
        colunms: "",
        dfindex: "",
        spacesep:false
      },
      csvcheckList:[],
      excelFormdata: {
        headerstart: null,
        colunms: "",
        dfindex: "",
        sheetname: ""
      },
      excelcheckList:[]
    };
  },
  methods: {
    afterupload(response, file, fileList) {
      //this.$refs.tab1.clearFiles()
      this.show = false;
      console.log(response);
      this.tablecolumn = response.columns;
      this.tableData = response.data;
      console.log(this.tableData);
    },
    handleBefore(file) {
      this.filepostdata["header"] = 1;
    },
    changeradio() {
      if (this.radio == "1") {
        this.flag = true;
      } else {
        this.flag = false;
      }
    },
    closeDialog(){
      this.csvFormdata={
        headerstart: null,
        sep: ",",
        colunms: "",
        dfindex: "",
        spacesep:false
      }
      this.excelFormdata= {
        headerstart: null,
        colunms: "",
        dfindex: "",
        sheetname: ""
      }
      this.csvcheckList=[]
      this.excelcheckList=[]
      this.flag=null
      this.radio="0"
    },
    changcheckbox(){
      console.log(this.csvcheckList)
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>
