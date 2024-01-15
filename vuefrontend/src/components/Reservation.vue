<template>
    <div class="table-responsive">
        <div class="jumbotron">
            <h4 class="text-center"><i class="fa-solid fa-book fa-m"></i> Reservation Application</h4>
            <p>
                This is a simple reservation application, made by Vuejs CDN and
                Django Rest-API Framework && Poetry Package Management,
                This allow you to (GET, CREATE, EDIT, DELETE) your details.
            </p>
        </div>
        <button type="button" class="btn btn-primary m-2 fload-end" data-bs-toggle="modal" data-bs-target="#exampleModal"
            @click="addClick()">
            <i class="fa-solid fa-add fa-lg"></i>
            Add Details
        </button>
        <table class="table table-bordered border-dark mt-2">
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
                    <th>
                        Info
                    </th>
                    <th>
                        Edit
                    </th>
                    <th>
                        Delete
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
                    <!-- Buttons like edit and delete -->
                    <td>
                        <button type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#exampleModalInfo"
                            @click="info(item)">
                            <i class="fa-solid fa-circle-info fa-lg"></i>
                        </button>
                        <div class="modal fade" id="exampleModalInfo" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" ref="modalPopup">
                            <div class="modal-dialog modal-m modal-dialog-centered" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">{{ modalTitle }} : {{ fname }}</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <ul class="list-unstyled">
                                            <li>First Name: <strong>{{ fname }}</strong></li>
                                            <li>Last Name: <strong>{{ lname }}</strong></li>
                                            <li>Email: <strong>{{ email }}</strong></li>
                                            <li>Phone: <strong>{{ phone }}</strong></li>
                                        </ul>
                                    </div>
                                    <div class="modal-footer">
                                          <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Close</button>
                                    </div>
                                </div>
                            </div>
                        </div> <!--- End Modal -->
                    </td>
                    <td>
                        <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#exampleModal"
                            @click="editClick(item)">
                            <i class="fa-solid fa-pen-to-square fa-lg"></i>
                        </button>
                    </td>
                    <td>
                        <button type="button" @click="deleteClick(item.userID)" class="btn btn-danger">
                            <i class="fa-solid fa-trash fa-lg"></i>
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" ref="modalPopup">
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
                        <button type="button" @click="createClick()" v-if="userID == 0" class="btn btn-success">
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
        info(item) {
            this.modalTitle = "Information";
            this.userID = item.userID;
            this.fname = item.fname;
            this.lname = item.lname;
            this.email = item.email;
            this.phone = item.phone;
        },
    },
    mounted: function () {
        this.refreshData();
    }
}
</script>
