@app.route("/sub/step6/<url>/finished",methods=["GET","POST"])
def CheckFinishedData(url):
    booking = Booking.query.filter_by(url=url).first()
    all_document = Document.query.filter_by(documentowner_id=booking.id).all()  
    if len(all_document) == 3 :
        booking.status = "pending payment"
        db.session.commit()
        return redirect(url_for("InvoiceId",url=url))