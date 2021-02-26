
class RedirectUserMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('accounts:indexAcc')
		else:
			return super().dispatch(request, *args, **kwargs)