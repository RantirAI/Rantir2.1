<template>
    <div class="ra-main">
        <div class="ra-header-container">
            <!-- Title Section -->
            <div class="ra-title-section">
                <h2>Subscriptions</h2>
                <span>New</span>
            </div>
            <!-- Buttons Section -->
            <div class="ra-buttons-container">
                <!-- Settings Button -->
                <a href="javascript:void(0)">
                    <button class="ra-nav-button">
                        <svg width="24px" height="24px" stroke-width="1.5" viewBox="0 0 24 24" fill="none"
                            xmlns="http://www.w3.org/2000/svg" color="#000000">
                            <path d="M12 11.5V16.5" stroke="#000000" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round"></path>
                            <path d="M12 7.51L12.01 7.49889" stroke="#000000" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round"></path>
                            <path
                                d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"
                                stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                            </path>
                        </svg>
                        View Issues
                    </button>
                </a>
                <a href="javascript:void(0)">
                    <button class="ra-nav-button">
                        <svg width="24px" height="24px" viewBox="0 0 24 24" stroke-width="1.5" fill="none"
                            xmlns="http://www.w3.org/2000/svg" color="#000000">
                            <path
                                d="M10.0503 10.6066L2.97923 17.6777C2.19818 18.4587 2.19818 19.725 2.97923 20.5061V20.5061C3.76027 21.2871 5.0266 21.2871 5.80765 20.5061L12.8787 13.435"
                                stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                            </path>
                            <path
                                d="M10.0502 10.6066C9.20638 8.45358 9.37134 5.6286 11.1109 3.88909C12.8504 2.14957 16.0606 1.76777 17.8284 2.82843L14.7877 5.8691L14.5051 8.98014L17.6161 8.69753L20.6568 5.65685C21.7175 7.42462 21.3357 10.6349 19.5961 12.3744C17.8566 14.1139 15.0316 14.2789 12.8786 13.435"
                                stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                            </path>
                        </svg>
                        Settings
                    </button>
                </a>

                <!-- Integrations Button -->

                <nuxt-link :to="{ name: 'flows' }">
                    <button class="ra-nav-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none">
                            <path
                                d="M15.75 5.51478L15.75 12.4852C15.75 12.6486 15.6614 12.7992 15.5185 12.8786L9.21854 16.3786C9.08263 16.4541 8.91737 16.4541 8.78146 16.3786L2.48146 12.8786C2.3386 12.7992 2.25 12.6486 2.25 12.4852L2.24999 5.51478C2.24999 5.35136 2.33859 5.20078 2.48145 5.12141L8.78146 1.62141C8.91737 1.54591 9.08263 1.54591 9.21854 1.62141L15.5185 5.12141C15.6614 5.20078 15.75 5.35136 15.75 5.51478Z"
                                stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            <path
                                d="M2.64633 5.47022L8.78147 8.87863C8.91739 8.95414 9.08264 8.95414 9.21855 8.87863L15.375 5.45837"
                                stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M9 15.75V 9" stroke="black" stroke-width="1.5" stroke-linecap="round"
                                stroke-linejoin="round" />
                        </svg>
                        Integrations
                    </button>
                </nuxt-link>


                <div class="ra-button-container">
                    <button class="ra-invoice-button">
                        <svg width="24px" height="24px" stroke-width="1.5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" color="#000000"><path d="M13.8476 13.317L9.50515 18.2798C8.70833 19.1905 7.29167 19.1905 6.49485 18.2798L2.15238 13.317C1.49259 12.563 1.49259 11.437 2.15238 10.683L6.49485 5.72018C7.29167 4.80952 8.70833 4.80952 9.50515 5.72017L13.8476 10.683C14.5074 11.437 14.5074 12.563 13.8476 13.317Z" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M13 19L17.8844 13.3016C18.5263 12.5526 18.5263 11.4474 17.8844 10.6984L13 5" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M17 19L21.8844 13.3016C22.5263 12.5526 22.5263 11.4474 21.8844 10.6984L17 5" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>
                        Invoices
                    </button>
                    <div class="ra-tooltip">
                        <span class="ra-tooltip-text">Coming soon</span>
                        <div class="ra-tooltip-arrow"></div>
                    </div>
                </div>

                <!-- View Runs Button -->
                <a href="/projects/qOCYXm38zKgAdsxblisdv/runs">
                    <button class="ra-nav-button">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" fill="none">
                            <path
                                d="M15 15C15.3978 15 15.7794 14.842 16.0607 14.5607C16.342 14.2794 16.5 13.8978 16.5 13.5V6C16.5 5.60218 16.342 5.22064 16.0607 4.93934C15.7794 4.65804 15.3978 4.5 15 4.5H9.075C8.82414 4.50246 8.57666 4.44196 8.35523 4.32403C8.13379 4.20611 7.94547 4.03453 7.8075 3.825L7.2 2.925C7.06342 2.7176 6.87748 2.54736 6.65887 2.42955C6.44027 2.31174 6.19583 2.25004 5.9475 2.25H3C2.60218 2.25 2.22064 2.40804 1.93934 2.68934C1.65804 2.97064 1.5 3.35218 1.5 3.75V13.5C1.5 13.8978 1.65804 14.2794 1.93934 14.5607C2.22064 14.842 2.60218 15 3 15H15Z"
                                stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
                        </svg>
                        Subscription Plans
                    </button>
                </a>
            </div>

            <!-- Add New Flow Section -->
            <div class="ra-new-flow-section">
                <button v-on:click="isOpenNewGroupModal = true" class="ra-new-flow-button">
                    New User Group
                </button>
            </div>
        </div>
        <!-- card code -->
        <div class="ra-snapshot">
            <h1>Snapshot of your Users</h1>
            <div class="ra-content">
                <div class="ra-main-driver">
                    <div class="ra-month">
                        <div class="ra-last">
                            <strong>
                                {{ subscriptionOverView?.total_members ? numberFormat(subscriptionOverView?.total_members) : 0 }}
                            </strong>
                            <div class="ra-last-content">
                                <span>
                                    0.09%
                                </span>
                                <em>Vs last month</em>
                            </div>
                        </div>
                        <div class="ra-low">
                            <h5>Total Members</h5>
                            <p>
                                These are members signed up across all applications
                            </p>
                        </div>
                    </div>
                    <div class="ra-month-main">
                        <div class="ra-month-sign">
                            <div class="ra-last">
                                <strong>
                                    {{ subscriptionOverView?.signups_last_month ? numberFormat(subscriptionOverView?.signups_last_month) : 0 }}
                                </strong>
                            </div>
                            <div class="ra-low">
                                <h5>Signups in the last month</h5>
                                <p>
                                    Start learning how powerful Rantir is.
                                </p>
                            </div>
                        </div>
                        <div class="ra-month-sign">
                            <div class="ra-last">
                                <strong>
                                    {{ subscriptionOverView?.paid_members ?? 0 }}
                                </strong>
                            </div>
                            <div class="ra-low">
                                <h5>Paid members</h5>
                                <p>
                                    These are members that
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="ra-main-driver">
                    <div class="ra-month">
                        <div class="ra-last">
                            <strong>
                                ${{ subscriptionOverView?.monthly_revenue ? numberFormat(subscriptionOverView?.monthly_revenue) : 0  }}
                            </strong>
                            <div class="ra-last-content">
                                <span>
                                    0.09%
                                </span>
                                <em>Vs last month</em>
                            </div>
                        </div>
                        <div class="ra-low">
                            <h5>Monthly revenue from subscriptions & invoices</h5>
                            <p>
                                Learn how to connect to your Stripe account and building revenue
                            </p>
                        </div>
                    </div>
                    <div class="ra-month-main">
                        <div class="ra-month-sign">
                            <div class="ra-last ra-autho">
                                <svg xmlns="http://www.w3.org/2000/svg" width="19" height="22" viewBox="0 0 19 22"
                                    fill="none">
                                    <path
                                        d="M0.0482496 3.85423L0.807304 18.7253C0.836042 19.2964 1.30751 19.7448 1.8794 19.7448H6.44786C6.82039 19.7448 7.09905 19.4028 7.0238 19.038L4.49616 6.99615C4.389 6.47655 4.97045 6.09191 5.40672 6.3938L11.9864 10.9467C12.3383 11.1902 12.3206 11.716 11.9532 11.9353L7.77175 14.4308C7.49631 14.5952 7.49181 14.9926 7.76345 15.1632L15.4276 19.7448C15.8247 19.9941 16.277 19.5174 16.0071 19.134L14.3338 16.952C14.0656 16.5711 14.1501 16.0458 14.5241 15.7682L18.2552 12.9986C18.6829 12.6811 18.8131 12.098 18.5611 11.6288L13.135 1.52509C12.9188 1.12247 12.4714 0.900895 12.0201 0.97295L0.951093 2.74026C0.409907 2.82667 0.0207101 3.30688 0.0482496 3.85423Z"
                                        fill="#141526" />
                                </svg>
                            </div>
                            <div class="ra-low">
                                <div class="ra-low-autho">
                                    <svg class="ml-[-10px]" width="100" height="22" viewBox="0 0 217 57" fill="none"
                                        xmlns="http://www.w3.org/2000/svg">
                                        <path
                                            d="M78.2658 47.9999L67.308 31.501H65.4402V47.9999H55.7899V4.41772H73.2227C82.9976 4.41772 88.0407 10.457 88.0407 18.0527C88.0407 24.4655 84.6164 29.4464 77.8923 31.0029L90.3443 47.9999H78.2658ZM65.4402 13.1964V23.4071H71.7908C75.6509 23.4071 77.83 21.9129 77.83 18.3018C77.83 15.0642 75.6509 13.1964 71.7908 13.1964H65.4402ZM103.401 48.9338C95.9293 48.9338 89.7655 43.704 89.7655 33.6178C89.7655 23.5316 95.9293 18.3018 103.401 18.3018C108.07 18.3018 110.996 20.2318 112.802 23.1581H112.926V19.2357H122.328V47.9999H112.926V44.0775H112.802C110.996 47.0038 108.07 48.9338 103.401 48.9338ZM106.015 40.3419C109.813 40.3419 112.677 37.727 112.677 33.6178C112.677 29.5086 109.813 26.8937 106.015 26.8937C102.28 26.8937 99.4158 29.5086 99.4158 33.6178C99.4158 37.727 102.28 40.3419 106.015 40.3419ZM145.92 18.3018C152.271 18.3018 156.754 21.9751 156.754 30.1935V47.9999H147.415V32.8084C147.415 28.5125 145.609 26.5824 142.123 26.5824C138.947 26.5824 136.581 28.4502 136.581 33.5555V47.9999H127.18V19.2357H136.395V23.5939H136.519C138.511 20.2318 141.873 18.3018 145.92 18.3018ZM179.102 27.0805H173.187V35.7347C173.187 38.4119 173.872 39.2835 176.3 39.2835H177.358V47.9999H173.436C167.584 47.9999 163.786 45.1982 163.786 38.2873V27.0805H158.182V19.2357H163.786V7.71752H173.187V19.2357H179.102V27.0805ZM192.133 4.47998V13.9435H182.047V4.47998H192.133ZM182.421 47.9999V19.2357H191.822V47.9999H182.421ZM215.988 18.364V27.7653H215.178C208.89 27.7653 206.337 30.069 206.337 37.4157V47.9999H196.936V19.2357H206.15V25.0881H206.275C207.956 20.3564 211.256 18.364 215.801 18.364H215.988Z"
                                            fill="#141526"></path>
                                        <path
                                            d="M0.12563 7.49533L2.09105 46.001C2.16546 47.4799 3.38625 48.6408 4.86702 48.6408H16.6962C17.6608 48.6408 18.3823 47.7553 18.1875 46.8106L11.6426 15.6307C11.3652 14.2853 12.8707 13.2894 14.0003 14.0711L31.0372 25.86C31.9483 26.4904 31.9025 27.8518 30.9511 28.4196L20.1241 34.8814C19.4109 35.307 19.3993 36.3359 20.1026 36.7776L39.9475 48.6408C40.9757 49.2865 42.1467 48.0521 41.4479 47.0593L37.1152 41.4095C36.4209 40.4232 36.6396 39.0631 37.6081 38.3442L47.2689 31.1729C48.3763 30.3508 48.7134 28.8411 48.0609 27.626L34.0112 1.4645C33.4514 0.421994 32.2928 -0.151737 31.1243 0.0348349L2.46336 4.61095C1.06207 4.83468 0.0543215 6.07808 0.12563 7.49533Z"
                                            fill="#141526"></path>
                                    </svg>
                                    <em>
                                        Autho
                                    </em>
                                </div>
                                <p>
                                    Start learning how powerful Rantir Autho is.
                                </p>
                            </div>
                        </div>
                        <div class="ra-month-sign">
                            <div class="ra-last ra-autho">
                                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="15" viewBox="0 0 22 15"
                                    fill="none">
                                    <path
                                        d="M0.00695125 0.902561L1.6351 14.3236C1.68221 14.7119 1.96115 15 2.28999 15H6.77279C7.02056 15 7.24756 14.8349 7.36103 14.5721L9.52041 10.196C9.66736 9.85565 10.0936 9.9391 10.1417 10.3176L10.7304 14.3288C10.7794 14.7147 11.0575 15 11.3847 15H15.8609C16.1141 15 16.3451 14.8277 16.4559 14.5561L21.9324 1.13505C22.1464 0.610653 21.8263 0 21.3375 0H17.395C17.1192 0 16.8723 0.204136 16.7755 0.512271L15.6153 4.2035C15.5341 4.46156 15.694 4.73684 15.925 4.73684H17.5405C17.8232 4.73684 17.9757 5.13241 17.7917 5.38847L14.121 9.87289C13.8993 10.1815 13.4785 9.93714 13.5454 9.53859L14.2105 6.19584C14.2514 5.95158 14.0948 5.72368 13.8861 5.72368H11.9265C11.7035 5.72368 11.5444 5.46598 11.6105 5.21195L12.7 1.02347C12.8321 0.515416 12.5139 0 12.068 0H8.78589C8.5135 0 8.26893 0.199149 8.16967 0.50179L7.02205 4.0009C6.93714 4.25978 7.09715 4.53947 7.33015 4.53947H8.78585C9.06636 4.53947 9.2196 4.92981 9.04002 5.18692L5.40892 9.76056C5.18645 10.0791 4.75548 9.82534 4.83202 9.42091L5.59625 6.008C5.64297 5.76113 5.48565 5.52632 5.27352 5.52632H3.49445C3.27012 5.52632 3.11082 5.26559 3.17947 5.01079L4.25164 1.03106C4.38894 0.521444 4.07034 0 3.62168 0H0.661837C0.258663 0 -0.050801 0.426502 0.00695125 0.902561Z"
                                        fill="#141526" />
                                </svg>
                            </div>
                            <div class="ra-low">
                                <h5>Integrate with Webtir</h5>
                                <p>
                                    Our sister product Webtir can spin up a website with AI
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="ra-embed ra-data">
                <h1>User Groups & Embed Links</h1>
                <div class="ra-table-container">
                    <table class="ra-custom-table">
                        <tbody>
                            <!-- Row 1 -->
                            <tr class="ra-table-row">
                                <td class="ra-table-cell">
                                    <div class="ra-cell-content">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="19" height="19"
                                            viewBox="0 0 19 19" fill="none">
                                            <g clip-path="url(#clip0_893_11138)">
                                                <path
                                                    d="M9.50065 1.58337C5.1284 1.58337 1.58398 5.12779 1.58398 9.50004C1.58398 13.8723 5.1284 17.4167 9.50065 17.4167C13.8729 17.4167 17.4173 13.8723 17.4173 9.50004C17.4173 5.12779 13.8729 1.58337 9.50065 1.58337Z"
                                                    stroke="black" stroke-width="1.5" stroke-linecap="round"
                                                    stroke-linejoin="round" />
                                                <path
                                                    d="M3.38086 14.5237C3.38086 14.5237 5.14551 12.2709 9.49967 12.2709C13.8538 12.2709 15.6185 14.5237 15.6185 14.5237"
                                                    stroke="black" stroke-width="1.5" stroke-linecap="round"
                                                    stroke-linejoin="round" />
                                                <path
                                                    d="M9.5 9.5C10.8117 9.5 11.875 8.43668 11.875 7.125C11.875 5.81332 10.8117 4.75 9.5 4.75C8.18832 4.75 7.125 5.81332 7.125 7.125C7.125 8.43668 8.18832 9.5 9.5 9.5Z"
                                                    stroke="black" stroke-width="1.5" stroke-linecap="round"
                                                    stroke-linejoin="round" />
                                            </g>
                                            <defs>
                                                <clipPath id="clip0_893_11138">
                                                    <rect width="19" height="19" fill="white" />
                                                </clipPath>
                                            </defs>
                                        </svg>
                                        <div class="ra-truk">
                                            <strong>Truck Users</strong>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                            <!-- Additional rows follow the same pattern -->
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="ra-embed">
                <h1>Connected User Databases</h1>
                <div class="ra-table-container">
                    <table class="ra-custom-table">
                        <tbody>
                            <!-- Row 1 -->
                            <tr class="ra-table-row">
                                <td class="ra-table-cell">
                                    <div class="ra-cell-content">
                                        <span class="icon-wrapper">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
                                                viewBox="0 0 20 20" fill="none">
                                                <path
                                                    d="M4.0957 9.83008V14.7451C4.0957 14.7451 4.0957 17.2027 9.82994 17.2027C15.5642 17.2027 15.5642 14.7451 15.5642 14.7451V9.83008"
                                                    stroke="#656565" stroke-width="1.22877" />
                                                <path
                                                    d="M4.0957 4.91504V9.8301C4.0957 9.8301 4.0957 12.2876 9.82994 12.2876C15.5642 12.2876 15.5642 9.8301 15.5642 9.8301V4.91504"
                                                    stroke="#656565" stroke-width="1.22877" />
                                                <path
                                                    d="M9.82994 2.45752C15.5642 2.45752 15.5642 4.91505 15.5642 4.91505C15.5642 4.91505 15.5642 7.37258 9.82994 7.37258C4.0957 7.37258 4.0957 4.91505 4.0957 4.91505C4.0957 4.91505 4.0957 2.45752 9.82994 2.45752Z"
                                                    stroke="#656565" stroke-width="1.22877" />
                                            </svg>
                                        </span>
                                        <div class="ra-truk">
                                            <strong>Truck Users</strong>
                                            <div class="ra-subtitle">
                                                <span>Database</span>
                                                <em class="ra-dot">•</em>
                                                <span>created 1 year ago</span>
                                            </div>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                            <!-- Additional rows follow the same pattern -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <UserGroupModal v-if="isOpenNewGroupModal" @close="isOpenNewGroupModal = false" />
       
    </div>
</template>

<script>
import modal from '@baserow/modules/core/mixins/modal'
import error from '@baserow/modules/core/mixins/error'
import { required } from 'vuelidate/lib/validators'
import Dropdown from '@baserow/modules/core/components/Dropdown';
import UserGroupModal from './userGroupModal.vue'
import { mapGetters } from 'vuex'
export default {
    name: 'Subscriptions',
    layout: 'app',
    mixins: [modal, error],
    components: {
        Dropdown,
        UserGroupModal
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
            databaselist: [{
                id: 1,
                name: 'Database 1'
            }, {
                id: 2,
                name: 'Database 2'
            }]
        }
    },
    computed: {
        ...mapGetters({
            subscriptionOverView: 'subscriptions/subscriotionOverview',
        })
    },
    methods: {
        numberFormat(value){
            return new Intl.NumberFormat().format(value)
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
        async getSubscriptionOverView(){
            await this.$store.dispatch('subscriptions/getSubscriptionOverview')
        }
    },
    created() {
        if(!this.subscriptionOverView){
            this.getSubscriptionOverView()
        }
    },
    validations: {
        group: {
            name: { required },
        },
    },
}
</script>