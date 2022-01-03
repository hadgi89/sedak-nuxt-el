<template>
  <div>
    
    <div class="brand">
      <el-link href="#" :underline="false">
        <el-image src="logo.svg" ></el-image>
      </el-link>
      
      <el-radio-group v-model="isCollapse">
        <el-radio-button :label="false" class="expand-aside"><i class="el-icon-s-unfold"></i></el-radio-button>
        <el-radio-button :label="true" class="collapse-aside"><i class="el-icon-s-fold"></i></el-radio-button>
      </el-radio-group>
    </div>
    
    

    <el-menu 
    class="aside" 
    @open="handleOpen" 
    @close="handleClose"
    background-color="#1F2937" 
    text-color="#9CA3AF" 
    active-text-color="#E5E7EB" 
    unique-opened default-active="2"
    :collapse="isCollapse">
      <el-menu-item index="1">
        <i class="el-icon-notebook-1"></i>
        <span>Проекты</span>
      </el-menu-item>

      <el-menu-item index="2">
        <i class="el-icon-suitcase-1"></i>
        <span>Должники</span>
      </el-menu-item>
      
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-receiving"></i>
          <!-- <i class="material-icons-two-tone">drafts</i> -->
          <span>Корреспонденция</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="3-1"><i class="el-icon-d-arrow-right"></i>Входящая</el-menu-item>
          <el-menu-item index="3-2"><i class="el-icon-d-arrow-right"></i>Исходящая</el-menu-item>
          <el-menu-item index="3-3"><i class="el-icon-d-arrow-right"></i>Корреспонденты</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-menu-item index="4">
        <i class="el-icon-coin"></i>
        <span>Разное</span>
      </el-menu-item>

      <el-submenu index="5">
        <template slot="title">
          <i class="el-icon-receiving"></i>
          <!-- <i class="material-icons-two-tone">drafts</i> -->
          <span>Корреспонденция</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="3-1"><i class="el-icon-d-arrow-right"></i>Входящая</el-menu-item>
          <el-menu-item index="3-2"><i class="el-icon-d-arrow-right"></i>Исходящая</el-menu-item>
          <el-menu-item index="3-3"><i class="el-icon-d-arrow-right"></i>Корреспонденты</el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>

  </div>
</template>


<script>

export default {
  name: "Aside",

  data() {
    return {
      isCollapse: false
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>


<style lang="css">

  .el-icon-d-arrow-right {
    font-size: 10px;
  }

  .brand {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    padding-left: 20px;
    height: 60px;
    background-color: #1F2937;
  }


  /* .el-menu {
    height: 100vh;
  } */

  .aside {
    height: 100vh;
  }
  .aside:not(.el-menu--collapse) {
    width: 250px;
    
  }
  
  
  </style>