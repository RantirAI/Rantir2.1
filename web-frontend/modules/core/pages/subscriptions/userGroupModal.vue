<template>
    <Modal>
        <div class="modal__wrapper">
            <div class="modal__box">
                <h2 class="box__title">
                    Create a New User Group
                </h2>
                <form @submit.prevent="createGroup">
                    <div class="row">
                        <div class="col col-12">
                            <FormGroup
                                small-label
                                required
                                :error="$v.group.name.$error"
                            >
                                <template #label>
                                    <i class="iconoir-text"></i>
                                    {{ $t('subscription.name') }}
                                </template>
                                <FormInput
                                    ref="name"
                                    v-model="group.name"
                                    :error="$v.group.name.$error"
                                    :disabled="success"
                                    size="large"
                                    @blur="$v.group.name.$touch()"
                                >
                                </FormInput>
                                <template #error>
                                    <i class="iconoir-warning-triangle"></i>
                                    {{ $t('error.thisFieldIsRequired') }}
                                </template>
                            </FormGroup>
                        </div>
                        <div class="col col-12">
                            <FormGroup
                                small-label
                                required
                                :error="$v.group?.database?.$error"
                            >
                                <template #label>
                                    <span class="new-lable">Select the Database this User Group should belong too</span>
                                    <Button
                                    @click=""
                                        type="transparent"
                                        size="tiny"
                                    >
                                    Create a New Database
                                    </Button>
                                </template>
    
                                <Dropdown v-model="group.database" placeholde="Select database" fixed-items @input="$emit('input', $event)">
                                    <DropdownItem
                                    v-for="database in databaselist"
                                    :key="database.id"
                                    :value="database.id"
                                    :name="database.name"
                                    />
                                </Dropdown>
                                <template #error>
                                    <i class="iconoir-warning-triangle"></i>
                                    {{ $t('error.thisFieldIsRequired') }}
                                </template>
                            </FormGroup>
                        </div>
                        <div class="col col-12">
                            <FormGroup
                                small-label
                                required
                                :error="$v.group?.plan?.$error"
                            >
                                <template #label>
                                    <span class="new-lable">Assign this User Group to Plans</span>
                                    <Button
                                    @click=""
                                        type="transparent"
                                        size="tiny"
                                    >
                                    Create a New Plan
                                    </Button>
                                </template>
    
                                <Dropdown v-model="group.plan" placeholde="Select Plan" fixed-items @input="$emit('input', $event)">
                                    <DropdownItem
                                    v-for="paln in planlist"
                                    :key="paln.id"
                                    :value="paln.id"
                                    :name="paln.name"
                                    />
                                </Dropdown>
                                <template #error>
                                    <i class="iconoir-warning-triangle"></i>
                                    {{ $t('error.thisFieldIsRequired') }}
                                </template>
                            </FormGroup>
                        </div>
                        <div class="col col-12">
                            <button class="new_group_button">Add another plan to this user group</button>
                        </div>
                        <div class="auth__action mb-32">
                            
                        </div>
                        <div class="col col-12 align-right">
                            <Button
                                type="action"
                                size="large"
                                :loading="loading"
                                :disabled="loading || success"
                            >
                                {{ $t('subscription.newUserGroup') }}
                            </Button>
                        </div>
                    </div>
                </form>
                <div class="modal__actions" v-on:click="$emit('close')">
                    <a class="modal__close">
                        <i class="iconoir-cancel"></i>
                    </a> 
                </div>
            </div>
        </div>
    </Modal>
</template>
<script>
import modal from '@baserow/modules/core/mixins/modal'
import error from '@baserow/modules/core/mixins/error'
import { required } from 'vuelidate/lib/validators'
import Dropdown from '@baserow/modules/core/components/Dropdown';
import subscriptionsService from '@baserow/modules/core/services/subscriptions';
import newPlanModal from './newPlanModal.vue';
export default {
    name: 'userGroupModal',
    mixins: [modal, error],
    components: {
        Dropdown,
        newPlanModal
    },
    data() {
        return {
            isOpenNewGroupModal: false,
            col1Width: 240,
            isCollapsed: false,
            loading: false,
            success: false,
            group: {
                name: '',
                database: '',
                plan: ''
            },
            databaselist: [],
            planlist: []
        }
    },
    computed: {

    },
    methods: {
        async getDatabaseList(){
            console.log('get database list')
            const response = await subscriptionsService(this.$client).getDatabases()
            this.databaselist = response.data
        },
        async getPlanList(){
            console.log('get database list')
            const response = await subscriptionsService(this.$client).getPlans()
            this.planlist = response.data
        },

        async createGroup() {
            this.$v.$touch()
            if (this.$v.$invalid) {
                return
            }
            this.loading = true
            this.hideError();
            try {
                await this.$store.dispatch('subscriptions/createNewUserGroup', this.group)
                this.loading = false
            } catch (error) {
                this.showError(error)
            }
            console.log('create group')
        },
        // async getdatabaselist() {
        //     try {
        //         await this.$store.dispatch('subscriptions/getDatabaseList')
        //     } catch (error) {
        //         this.showError(error)
        //     }
        // }
    },
    mounted() {
        this.getDatabaseList();
        this.getPlanList();
    },
    validations: {
        group: {
            name: { required },
            database: { required },
            plan: { required },
        }
    },
}
</script>