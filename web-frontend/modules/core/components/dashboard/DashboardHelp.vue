<template>
  <Alert
    v-if="displayAlert"
    type="blank"
    close-button
    position="bottom"
    :width="396"
    @close="handleAlertClose"
  >
    <template #image
      ><img
        src="@baserow/modules/core/assets/images/dashboard_alert_image.png"
        srcset="
          @baserow/modules/core/assets/images/dashboard_alert_image@2x.png 2x
        "
      />
    </template>
    <template #title
      ><h4>{{ $t('dashboard.alertTitle') }}</h4></template
    >
    <p>{{ $t('dashboard.alertText') }}</p>
    <template #actions>
      <Button
        tag="a"
        href="https://gitlab.com/rantir/rantir"
        target="_blank"
        rel="noopener noreferrer"
        type="secondary"
        style="background-color:white;color:black;"

      >
      <img
        src="@baserow/modules/core/static/img/devtir.png"
        class="mr-4"

      /> {{ $t('dashboard.starOnGitlab') }}</Button
      >
      <ButtonIcon
        v-tooltip="$t('dashboard.shareOnTwitter')"
        tag="a"
        tooltip-position="top"
        href="https://x.com/rantircloud"
        target="_blank"
        rel="noopener noreferrer"
        icon="baserow-icon-twitter"
      ></ButtonIcon>
      <ButtonIcon
        v-tooltip="$t('dashboard.shareOnReddit')"
        tag="a"
        tooltip-position="top"
        icon="baserow-icon-reddit"
        href="https://www.reddit.com/r/rantir/"
        target="_blank"
        rel="noopener noreferrer"
      ></ButtonIcon>
      <ButtonIcon
        v-tooltip="$t('dashboard.shareOnFacebook')"
        tag="a"
        tooltip-position="top"
        icon="baserow-icon-facebook"
        href="https://www.facebook.com/profile.php?id=61568494167115"
        target="_blank"
        rel="noopener noreferrer"
      ></ButtonIcon>
      <ButtonIcon
        v-tooltip="$t('dashboard.shareOnLinkedIn')"
        tag="a"
        tooltip-position="top"
        icon="baserow-icon-linkedin"
        href="https://www.linkedin.com/company/rantir"
        target="_blank"
        rel="noopener noreferrer"
      ></ButtonIcon>
    </template>
  </Alert>
</template>

<script>
const helpDisplayCookieName = 'baserow_dashboard_alert_closed'

export default {
  name: 'DashboardHelp',
  data() {
    return {
      showAlert: true,
    }
  },
  computed: {
    displayAlert() {
      return this.showAlert && !this.$cookies.get(helpDisplayCookieName)
    },
  },
  methods: {
    handleAlertClose() {
      this.showAlert = false
      this.$cookies.set(helpDisplayCookieName, true, {
        path: '/',
        maxAge: 60 * 60 * 24 * 182, // 6 months
      })
    },
  },
}
</script>
