Vue.component('memcache-row', {

	template: `
		<div>
			<div class="key" @click="setShowing"><slot name="key"></slot></div>
			<div :class="{ 'hidden': !showing }"><slot name="value"></slot></div>
		</div>`,

	data() {

		return {
			showing: false
		}

	},

	methods: {
		
		setShowing() {

			this.showing = true;

		}

	}
});

new Vue({

	el: '#root'

});

