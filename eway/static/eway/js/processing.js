(function () {
    var eway = eway || {};

    eway.processing = {
        orderFormId: null,
        ewayFormId: null,
        init: function (options) {
            options = options || {};

            var ep = eway.processing;

            ep.orderFormId = options.orderFormId || "#place-order-form";
            ep.ewayFormId = options.ewayFormId || "#eway-form";

            console.log('initialising');
            var form = $(ep.orderFormId);

            form.submit(function (ev) {
                ev.preventDefault();
                $(this).unbind('submit');
                console.log("submitting form to eWay");
                eway.processing.processTransaction($(ep.ewayFormId)[0]);
            });
        },
        processTransaction: function (form) {
            // call eWAY to process the request
            eWAY.process(form, {
                autoRedirect: false,
                onComplete: function (data) {
                    eway.processing.handleResponse(data);
                },
                onError: function (e) {
                    eway.processing.handleResponse(data);
                },
                onTimeout: function (e) {
                    eway.processing.handleResponse(data);
                }
            });
        },
        handleResponse: function (data) {
            var ep = eway.processing,
                orderForm = $(ep.orderFormId);

            $(ep.ewayFormId).remove();
            $('input[name=access_code]', orderForm).val(data.AccessCode);
            orderForm.submit();
        }
    };

    eway.processing.init();
})();
