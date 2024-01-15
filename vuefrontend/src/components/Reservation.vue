<template>
        <div class="table-responsive">
            <div class="jumbotron">
                <h4 class="text-center">Reservation Application</h4>
                <p>
                    This is a simple reservation application, made by Vuejs CDN and
                    Django Rest-API Framework && Poetry Package Management,
                    This allow you to (GET, CREATE, EDIT, DELETE) your details.
                </p>
            </div>
            <button type="button" class="btn btn-primary m-2 fload-end" data-bs-toggle="modal" data-bs-target="#exampleModal"
                @click="addClick()">
                Add Details
            </button>
            <table class="table">
                <thead>
                    <tr>
                        <th>
                            User ID
                        </th>
                        <th>
                            First Name
                        </th>
                        <th>
                            Last Name
                        </th>
                        <th>
                            Email
                        </th>
                        <th>
                            Phone
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <!-- eslint-disable -->
                    <tr v-for="item in reservations" :key="item.userID">
                        <td>{{ item.userID }}</td>
                        <td>{{ item.fname }}</td>
                        <td>{{ item.lname }}</td>
                        <td>{{ item.email }}</td>
                        <td>{{ item.phone }}</td>
                        <td>
                            <!-- Buttons like edit and delete -->
                            <button type="button" class="btn btn-light mr-1" data-bs-toggle="modal"
                                data-bs-target="#exampleModal" @click="editClick(item)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-pencil-square" viewBox="0 0 16 16">
                                    <path
                                        d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                                    <path fill-rule="evenodd"
                                        d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z" />
                                </svg>
                            </button>
                            <button type="button" @click="deleteClick(item.userID)" class="btn btn-light mr-1">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                    class="bi bi-trash-fill" viewBox="0 0 16 16">
                                    <path
                                        d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z" />
                                </svg>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-m modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">{{ modalTitle }}</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="d-flex flex-row bd-highlight mb-3">
                                <div class="w-100 bd-highlight">
                                    <div class="input-group mb-3">
                                        <span class="input-group-text">First Name</span>
                                        <input type="text" class="form-control" v-model="fname">
                                    </div>
                                    <div class="input-group mb-3">
                                        <span class="input-group-text">Last Name</span>
                                        <input type="text" class="form-control" v-model="lname">
                                    </div>
                                    <div class="input-group mb-3">
                                        <span class="input-group-text">Email</span>
                                        <input type="phone" class="form-control" v-model="email">
                                    </div>
                                    <div class="input-group mb-3">
                                        <span class="input-group-text">Phone</span>
                                        <input type="phone" class="form-control" v-model="phone">
                                    </div>
                                </div>
                            </div>
                            <button type="button" @click="createClick()" v-if="userID == 0" class="btn btn-primary">
                                Create
                            </button>
                            <button type="button" @click="updateClick()" v-if="userID != 0" class="btn btn-primary">
                                Update
                            </button>
                        </div>
                    </div>
                </div>
            </div> <!--- End Modal -->
        </div>
</template>

<script>
    import axios from 'axios';
    const variables = {
        API_URL: "http://127.0.0.1:8000/"
    };

    export default {
         /* eslint-disable */
        name: 'Reservation',
        data() {
            return {
                reservations: [],
                modalTitle: "",
                userID: 0,
                fname: "",
                lname: "",
                email: "",
                phone: "",
            }
        },
        methods: {
            refreshData() {
                axios.get(variables.API_URL + "reservation")
                    .then((response) => {
                        this.reservations = response.data;
                    });
            },
            addClick() {
                this.modalTitle = "Add Page";
                this.userID = 0;
                this.fname = "";
                this.lname = "";
                this.email = "";
                this.phone = "";
            },
            editClick(item) {
                this.modalTitle = "Edit Page";
                this.userID = item.userID;
                this.fname = item.fname;
                this.lname = item.lname;
                this.email = item.email;
                this.phone = item.phone;
            },
            createClick() {
                axios.post(variables.API_URL + "reservation", {
                    fname: this.fname,
                    lname: this.lname,
                    email: this.email,
                    phone: this.phone
                })
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            updateClick() {
                axios.put(variables.API_URL + "reservation", {
                    userID: this.userID,
                    fname: this.fname,
                    lname: this.lname,
                    email: this.email,
                    phone: this.phone
                })
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });
            },
            deleteClick(id) {
                if (!confirm("Are you sure?")) {
                    return;
                }
                axios.delete(variables.API_URL + "reservation/" + id)
                    .then((response) => {
                        this.refreshData();
                        alert(response.data);
                    });

            },
        },
        mounted: function () {
            this.refreshData();
        }
    }
</script>