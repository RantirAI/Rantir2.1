<template>
<div class="modal__wrapper">
    <div class="modal__box">
        <h2 class="box__title">
            Create a New Plan
        </h2>
        <form @submit.prevent="createGroup">
            <div class="row">
                <div class="col col-12">
                    <FormGroup
                        small-label
                        required
                        :error="$v.plan.name.$error"
                    >
                        <template #label>
                            <i class="iconoir-text"></i>
                            {{ $t('subscription.name') }}
                        </template>
                        <FormInput
                            ref="name"
                            v-model="plan.name"
                            :error="$v.plan.name.$error"
                            :disabled="success"
                            size="large"
                            @blur="$v.plan.name.$touch()"
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
                        :error="$v.plan?.database?.$error"
                    >
                        <template #label>
                            <span class="new-lable">Select the Database this User Group should belong too</span>
                        </template>
                        <Dropdown v-model="plan.database" placeholde="Select database" fixed-items @input="$emit('input', $event)">
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
                        :label="'Set a Price'" 
                        :error="$v.plan?.plan?.$error"
                    >
                        <template #label>
                            <span class="new-lable"></span>
                        </template>
                        <template v-for="(priceOption, index) in plan.priceOption">
                            <Dropdown v-model="priceOption.price" placeholde="Select Plan" fixed-items @input="$emit('input', $event)">
                                <DropdownItem
                                v-for="paln in planlist"
                                :key="paln.id"
                                :value="paln.id"
                                :name="paln.name"
                                />
                            </Dropdown>
                        </template>
                        <template #error>
                            <i class="iconoir-warning-triangle"></i>
                            {{ $t('error.thisFieldIsRequired') }}
                        </template>
                    </FormGroup>
                </div>
                <div class="col col-12">
                    <button @click.prevent="addNewPriceOption" class="new_group_button">Add another price to this plan</button>
                </div>
                <div class="col col-12">
                    <FormGroup
                        small-label
                        :label="'Set a Description'"
                        :error="$v.plan.description.$error"
                    >
                        <FormInput
                            ref="description"
                            v-model="paln.description"
                            :error="$v.paln.description.$error"
                            :disabled="success"
                            size="large"
                            @blur="$v.paln.description.$touch()"
                        >
                        </FormInput>
                        <template #error>
                            <i class="iconoir-warning-triangle"></i>
                            {{ $t('error.thisFieldIsRequired') }}
                        </template>
                    </FormGroup>
                </div>
                <div class="col col-12 align-right">
                    <Button
                        type="action"
                        size="large"
                        :loading="loading"
                        :disabled="loading || success"
                    >
                        Create Plan
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
</template>
<script>
import modal from '@baserow/modules/core/mixins/modal'
import error from '@baserow/modules/core/mixins/error'
import { required } from 'vuelidate/lib/validators'
import Dropdown from '@baserow/modules/core/components/Dropdown';
import subscriptionsService from '@baserow/modules/core/services/subscriptions'
export default {
    name: 'newPlanModal',
    mixins: [modal, error],
    components: {
        Dropdown
    },
    data() {
        return {
            loading: false,
            success: false,
            plan: {
                name: '',
                database: '',
                priceOption: [{
                    price:'',
                }],
                description: '',
                icon:'',
                image:'',
            },
            databaselist: [],
        }
    },
    methods: {
        addNewPriceOption() {
            this.group.priceOption.push({
                price: '',
            })
        },
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
        async createPlan() {
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
    },
    mounted() {
        this.getDatabaseList();
        this.getPlanList();
    },
    validations: {
        plan: {
            name: { required },
            database: { required },
            plan: { required },
            priceOption: {
                price: { required },
            },
        }
    },
}
</script>