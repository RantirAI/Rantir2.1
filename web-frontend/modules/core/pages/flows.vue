<template>
  <div class="layout">
    <div class="content">
      <div class="flows-container">
        <iframe :src="iframeSrc" frameborder="0" class="flows-iframe"></iframe>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Flows',
  layout: 'app',
  data() {
    return {
      col1Width: 240,
      isCollapsed: false,
    }
  },
  computed: {
    iframeSrc() {
      const refreshToken = this.$store.getters['auth/refreshToken'];
      return `http://localhost:4200/auth-callback?authToken=${refreshToken}`;
      // return `${this.$config.PUBLIC_ACTIVE_PIECES_URL}/auth-callback?authToken=${refreshToken}`;
    }
  },
  mounted() {
    console.log('URL',this.$config.PUBLIC_WEB_FRONTEND_URL,'---', this.$config.PUBLIC_ACTIVE_PIECES_URL)
  },
}
</script>

<style scoped>
.flows-container {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.flows-iframe {
  width: 100%;
  height: 100%;
}
.layout {
  display: flex;
}
.content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}
</style> 