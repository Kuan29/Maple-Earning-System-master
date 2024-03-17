<template>
    <q-page>
        <div class="row justify-center items-center fullscreen" id="index-bg"></div>
        <div class="q-pa-xl row justify-center items-center">
            <q-input class="col-4" v-model="text" label="캐릭터명" counter clearable filled autofocus>
                <template v-slot:append>
                    <q-icon name="search" class="cursor-pointer" />
                </template>
            </q-input>
        </div>
        <div class="row">
            <div class="q-pa-md row col-12 justify-center items-center q-gutter-md">
                <q-card class="bg-purple text-white shadow-4">
                    <q-card-section>
                        <div class="text-h6">
                            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Labore ipsum sunt, mollitia ipsa eligendi non repellat eius quis
                            voluptatem corrupti quod deserunt harum corporis asperiores eos ad, repellendus laboriosam explicabo.
                        </div>
                        <div class="text-subtitle2">by John Doe</div>
                    </q-card-section>
                </q-card>

                <q-card class="bg-pink text-white shadow-4">
                    <q-card-section>
                        <div class="text-h6">Our Changing Planet</div>
                        <div class="text-subtitle2">by John Doe</div>
                    </q-card-section>
                </q-card>

                <q-card class="bg-indigo text-white shadow-4">
                    <q-card-section>
                        <div class="text-h6">Our Changing Planet</div>
                        <div class="text-subtitle2">by John Doe</div>
                    </q-card-section>
                </q-card>

                <q-card class="bg-red text-white shadow-4">
                    <q-card-section>
                        <div class="text-h6">Our Changing Planet</div>
                        <div class="text-subtitle2">by John Doe</div>
                    </q-card-section>
                </q-card>

                <q-card class="bg-cyan text-white shadow-4">
                    <q-card-section>
                        <div class="text-h6">Our Changing Planet</div>
                        <div class="text-subtitle2">by John Doe</div>
                    </q-card-section>
                </q-card>
            </div>
        </div>
    </q-page>
</template>

<script>
export default {
    name: 'IndexPage',
    data() {
        return {
            text: ''
        }
    }
}
</script>

<style lang="scss" scoped>
.q-page {
    #index-bg {
        position: absolute;
        background-image: url('assets/background-01.jpg');
        background-repeat: no-repeat;
        background-size: cover;
        background-position: center;
        filter: blur(3px);
        opacity: 0.7;
        z-index: -1;
    }
}
</style>
