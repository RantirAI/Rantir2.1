<template>
  <div
    :key="elementType.name"
    v-tooltip="disabled ? disabledMessage : null"
    class="add-element-card"
    :class="{ 'add-element-card--disabled': disabled }"
    v-on="$listeners"
  >
    <div v-if="loading" class="loading"></div>
    <template v-else>
      <div class="add-element-card__content">
        <div class="add-element-card__element-type">
          <i
            class="add-element-card__element-type-icon"
            :class="elementType.iconClass"
          ></i>
        </div>
        <div class="add-element-card__name">
          <span>{{ elementType.name }}</span>
        </div>
      </div>
    </template>
  </div>
 </template>

 <script>
 export default {
   name: 'AddElementCard',
   props: {
     elementType: {
       type: Object,
       required: true,
     },
     loading: {
       type: Boolean,
       required: false,
       default: false,
     },
     disabledMessage: {
       type: String,
       required: false,
       default: '',
     },
     disabled: {
       type: Boolean,
       required: false,
       default: false,
     },
   },
 }
 </script>

 <style scoped>
 .add-element-card {
   display: flex;
   justify-content: center;
   align-items: center;
   text-align: center;
 }

 .add-element-card__content {
   display: flex;
   flex-direction: column;
   align-items: center;
   justify-content: center;
 }

 .add-element-card__element-type {
   display: flex;
   justify-content: center;
   align-items: center;
   margin-bottom: 0.5rem;
 }

 .add-element-card__element-type-icon {
   font-size: 2rem; /* Adjust size as needed */
 }

 .add-element-card__name {
   text-align: center;
 }

 .add-element-card--disabled {
   opacity: 0.5;
   cursor: not-allowed;
 }
 </style>
