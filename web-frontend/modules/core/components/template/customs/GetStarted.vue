<template>
  <div class="template-illustration">
    <div class="template-illustration__container">
      <div class="template-intro__content">
        <h1 class="template-intro__title">
          Build Software not Websites with AI & Rantir
        </h1>
        <p class="template-intro__description">
          Start using Rantir and experience a new way to let code & AI do all types of your tasks
        </p>
        <div class="template-intro__actions">
          <!-- Start a New Project Button -->
          <span ref="createApplicationContextLink">
            <Button
              icon="iconoir-plus"
              tag="a"
              @click="
                $refs.createApplicationContext.toggle(
                  $refs.createApplicationContextLink
                )
              "
            >
              Start a New Project
            </Button>
          </span>

          <!-- Go Enterprise Button -->
          <Button
            style="background-color: white; color: black;"
            tag="a"
            @click="showCreateMenu"
          >
            Go Enterprise
          </Button>
        </div>
      </div>
      <div
        class="template__illustration-image"
        v-html="
          require(`@baserow/modules/core/assets/images/template_illustration_getstarted_mix.svg?raw`)
        "
      />
    </div>

    <!-- Dropdown Menu -->
    <Context
      ref="createContext"
      :right="0"
      :top="0"
    >
      <ul class="dropdown__items">
        <li
          v-for="item in createOptions"
          :key="item.value"
          class="dropdown__item"
          @click="$emit('create', item.value)"
        >
          <i class="dropdown__item-icon" :class="item.icon"></i>
          {{ item.name }}
        </li>
      </ul>
    </Context>

    <CreateApplicationContext
      ref="createApplicationContext"
      :workspace="workspace"
    ></CreateApplicationContext>
  </div>
</template>

<script>
import CreateApplicationContext from '@baserow/modules/core/components/application/CreateApplicationContext'
import Context from '@baserow/modules/core/components/Context'
import Button from '@baserow/modules/core/components/Button'

export default {
  name: 'TemplateIntro',
  components: {
    Context,
    CreateApplicationContext,
    Button
  },
  computed: {
    workspace() {
      // Get the first workspace or the selected workspace from Vuex store
      return this.$store.getters['workspace/getAll'][0] || null
    }
  },
  // Remove the workspace prop since we're now getting it from the store
  props: {
    // ... other props if any
  },
  // Add error handling for when workspace isn't available
  mounted() {
    if (!this.workspace) {
      console.warn('No workspace available')
      // Optionally redirect to workspace creation or show an error message
    }
  },
  data() {
    return {
      // Dropdown options
      createOptions: [
        { name: 'Database', value: 'database', icon: 'fas fa-database' },
        { name: 'Table', value: 'table', icon: 'fas fa-table' },
        { name: 'Form', value: 'form', icon: 'fas fa-wpforms' },
      ],
    };
  },
  methods: {
    /**
     * Show the dropdown menu.
     * Ensures the Context component is toggled.
     */
    showCreateMenu(event) {
      this.$refs.createContext.toggle(event.target, 'bottom', 'left');
    },
  },
};
</script>

<style scoped>
/* Positioning for the illustration image */
.template__illustration-image {
  position: absolute;
  right: 40px;
  top: 50%;
  transform: translateY(-50%);
  width: 300px;
}

/* Overall container */
.template-illustration {
  position: relative;
}

/* Styling for the dropdown */
.dropdown__items {
  position: absolute;
  background: white;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  list-style: none;
  padding: 0;
  margin: 0;
  z-index: 1000;
  min-width: 200px;
}

.dropdown__item {
  padding: 10px 15px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  color: #333;
}

.dropdown__item:hover {
  background-color: #f5f5f5;
}

.dropdown__item-icon {
  font-size: 16px;
  color: #666;
}
</style>
