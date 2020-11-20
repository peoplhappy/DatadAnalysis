<template>
  <div id="app">
    <!-- <router-view/> -->
    <el-tabs
      v-model="editableTabsValue"
      type="card"
      @tab-click="handleClick"
      addable
      @tab-add="addtabpane"
      closable
      @tab-remove="removeTabPane"
    >
      <el-tab-pane
        v-for="item in editableTabs"
        :key="item.name"
        :label="item.title"
        :name="item.name"
      ><router-view/></el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      editableTabsValue: "1",
      editableTabs: [{
          title: 'Tab 1',
          name: '1',
          content: 'Tab 1 content'
        }
      ],
      tabIndex: 1
    };
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
    addtabpane(targetName) {
        let newTabName = ++this.tabIndex + '';
        this.editableTabs.push({
          title: 'New Tab',
          name: newTabName,
          content: 'New Tab content'
        });
        this.editableTabsValue = newTabName;
    },
    removeTabPane(currentkey){
        let tabs = this.editableTabs;
        let activeName = this.editableTabsValue;
        if (activeName === currentkey) {
          tabs.forEach((tab, index) => {
            if (tab.name === currentkey) {
              let nextTab = tabs[index + 1] || tabs[index - 1];
              if (nextTab) {
                activeName = nextTab.name;
              }
            }
          });
        }
        
        this.editableTabsValue = activeName;
        this.editableTabs = tabs.filter(tab => tab.name !== currentkey);
    }
  }
};
</script>

<style>
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
