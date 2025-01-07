<template>
  <div class="sidebar" :class="{
    'sidebar--collapsed': collapsed,
    'sidebar--dark': isDarkTheme
  }">
    <component
      :is="component"
      v-for="(component, index) in impersonateComponent"
      :key="index"
    ></component>

    <template v-if="showAdmin">
      <div class="sidebar__head">
        <a href="#" class="sidebar__back" @click="setShowAdmin(false)">
          <i class="sidebar__back-icon iconoir-nav-arrow-left"></i>
        </a>
        <div v-show="!collapsed" class="sidebar__title">
          {{ $t('sidebar.adminSettings') }}
        </div>
      </div>
      <SidebarAdmin v-show="!collapsed"></SidebarAdmin>
    </template>

    <template v-if="!showAdmin">
      <!-- Custom bottom tab -->
      <a
        ref="workspaceContextAnchor"
        class="sidebar__workspaces-selector"
        @click="
          $refs.workspacesContext.toggle(
            $refs.workspaceContextAnchor,
            'bottom',
            'left',
            8,
            16
          )
        "
      >
        <img
          v-show="!collapsed"
          :src="isDarkTheme
            ? require('@baserow/modules/core/static/img/logoOnly-old.svg')
            : require('@baserow/modules/core/static/img/logoOnly.svg')"
          style="height: 30px; width: 30px; object-fit: contain"
        />
        <Avatar
          :initials="selectedWorkspace.name || name | nameAbbreviation"
          style="height: 30px; width: 30px"
        ></Avatar>

        <span
          v-show="!collapsed"
          class="sidebar__workspaces-selector-selected-workspace"
          >{{ selectedWorkspace.name || name }}</span
        >
        <span
          v-show="!collapsed"
          v-if="unreadNotificationsInOtherWorkspaces"
          class="sidebar__unread-notifications-icon"
        ></span>
        <i
          v-show="!collapsed"
          class="sidebar__workspaces-selector-icon baserow-icon-up-down-arrows"
        ></i>
      </a>
      <SidebarUserContext
        ref="workspacesContext"
        :workspaces="workspaces"
        :selected-workspace="selectedWorkspace"
        @toggle-admin="setShowAdmin($event)"
      ></SidebarUserContext>
      <!-- End custom bottom tab -->

      <SidebarMenu
        v-show="!collapsed"
        v-if="hasSelectedWorkspace"
        :selected-workspace="selectedWorkspace"
      ></SidebarMenu>

      <SidebarWithWorkspace
        v-show="!collapsed"
        v-if="hasSelectedWorkspace"
        :applications="applications"
        :selected-workspace="selectedWorkspace"
      ></SidebarWithWorkspace>

      <SidebarWithoutWorkspace
        v-show="!collapsed"
        v-if="!hasSelectedWorkspace"
        :workspaces="workspaces"
      ></SidebarWithoutWorkspace>
    </template>

    <SidebarFoot
      :collapsed="collapsed"
      :width="width"
      @set-col1-width="$emit('set-col1-width', $event)"
    ></SidebarFoot>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import SidebarUserContext from '@baserow/modules/core/components/sidebar/SidebarUserContext';
import SidebarWithWorkspace from '@baserow/modules/core/components/sidebar/SidebarWithWorkspace';
import SidebarWithoutWorkspace from '@baserow/modules/core/components/sidebar/SidebarWithoutWorkspace';
import SidebarAdmin from '@baserow/modules/core/components/sidebar/SidebarAdmin';
import SidebarFoot from '@baserow/modules/core/components/sidebar/SidebarFoot';
import SidebarMenu from '@baserow/modules/core/components/sidebar/SidebarMenu';
import SidebarAdminItem from './SidebarAdminItem.vue';

export default {
  name: 'Sidebar',
  components: {
    SidebarAdmin,
    SidebarWithoutWorkspace,
    SidebarWithWorkspace,
    SidebarUserContext,
    SidebarMenu,
    SidebarFoot,
  },
  props: {
    applications: {
      type: Array,
      required: true,
    },
    workspaces: {
      type: Array,
      required: true,
    },
    selectedWorkspace: {
      type: Object,
      required: true,
    },
    collapsed: {
      type: Boolean,
      required: false,
      default: () => false,
    },
    width: {
      type: Number,
      required: false,
      default: 240,
    },
  },
  data() {
    return {
      showAdmin: false,
      isDarkTheme: false,
    };
  },
  beforeCreate() {
    // Add script to head to prevent flash
    if (process.client) {
      const savedTheme = localStorage.getItem('sidebarTheme')
      if (savedTheme === 'dark') {
        document.documentElement.classList.add('dark-theme')
      }
    }
  },
  created() {
    if (process.client) {
      const savedTheme = window.localStorage.getItem('sidebarTheme')
      this.isDarkTheme = savedTheme === 'dark'
    }
  },
  computed: {
    SidebarAdminItem() {
      return SidebarAdminItem;
    },
    impersonateComponent() {
      return Object.values(this.$registry.getAll('plugin'))
        .map((plugin) => plugin.getImpersonateComponent())
        .filter((component) => component !== null);
    },
    hasSelectedWorkspace() {
      return Object.prototype.hasOwnProperty.call(this.selectedWorkspace, 'id');
    },
    ...mapGetters({
      name: 'auth/getName',
      unreadNotificationsInOtherWorkspaces:
        'notification/anyOtherWorkspaceWithUnread',
    }),
  },
  methods: {
    setShowAdmin(value) {
      this.showAdmin = value;
      this.$forceUpdate();
    },
    toggleTheme(value) {
      this.isDarkTheme = value;
      if (process.client) {
        window.localStorage.setItem('sidebarTheme', this.isDarkTheme ? 'dark' : 'light');
        document.documentElement.classList.toggle('dark-theme', this.isDarkTheme);
      }
    },
  },
};
</script>

<style>
/* Add this outside of scoped to affect document root */
:root.dark-theme .sidebar {
  background-color: #1a1a1a !important;
  color: #ffffff !important;
}

/* Add styles for list items in dark mode */
:root.dark-theme .sidebar li.active,
:root.dark-theme .sidebar li:active {
  color: #ffffff !important;
  font-weight: bold !important;
}

:root.dark-theme .sidebar li.active a,
:root.dark-theme .sidebar li:active a {
  color: #ffffff !important;
  font-weight: bold !important;
}

/* Prevent flash of wrong theme */
.sidebar {
  transition: background-color 0.3s ease;
}
</style>

<style scoped>
.sidebar {
  background-color: #f8f9fa;
  color: #333;
  transition: all 0.3s ease;
}

.sidebar--dark {
  background-color: #1a1a1a;
  color: #ffffff;
}

.sidebar__theme-toggle {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
}

.theme-toggle-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 8px;
  color: inherit;
}

.theme-icon {
  font-size: 20px;
}
</style>

/* Prevent flash of light mode */
body.sidebar--dark {
  background-color: #1a1a1a;
  color: #ffffff;
  transition: none;
}
</style>

