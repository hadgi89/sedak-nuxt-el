<template>
  <div class="header-wrapper">

    <el-dropdown trigger="click">
      <span class="el-dropdown-link">
        <el-avatar :size="40" src="img/user/avatar-2.jpg"></el-avatar>
        Adam William
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-user"></i> -->
          <span class="material-icons-two-tone">account_circle</span>
          My Account
        </el-dropdown-item>
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-setting"></i> -->
          <span class="material-icons-two-tone">settings</span>
          Settings
        </el-dropdown-item>
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-bangzhu"></i> -->
          <span class="material-icons-two-tone">support</span>
          Support
        </el-dropdown-item>
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-lock"></i> -->
          <span class="material-icons-two-tone">lock</span>
          Lock
        </el-dropdown-item>
        <el-dropdown-item class="dropdown-item">
          <!-- <i class="el-icon-notebook-2"></i> -->
          <span class="material-icons-two-tone">chrome_reader_mode</span>
          Logout
        </el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>


  </div>
</template>

<script>
  export default {
    name: "Header",
  }
</script>


<style lang="css" scoped>

  .header-wrapper {
    display: inline-flex;
    align-items: center;
    justify-content: flex-end;
    width: 100%;
    height: 100%;
    background-color: #FFFFFF;
  }

  .el-dropdown-link {
    cursor: pointer;
  }


  .material-icons-two-tone {
    vertical-align: middle;
  }

  .dropdown-item.active, 
  .dropdown-item:active,
  .dropdown-item:hover, 
  .dropdown-item:focus {
    color: #7E57C2;
    text-decoration: none;
    background-color: #E8EAF6;
  }


</style>