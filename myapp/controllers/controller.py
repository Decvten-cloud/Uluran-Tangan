from flask import request, jsonify, redirect, url_for, render_template, session, flash
from myapp.models.model import create_user, get_user_by_email,tambah_donasi,verify_password,get_user_donasi

def beranda():
    return render_template('beranda.html')

def donasikonten1():
    return render_template('donasikonten1.html')

def donasikonten2():
    return render_template('donasikonten2.html')

def donasikonten3():
    return render_template('donasikonten3.html')

def donasikonten4():
    return render_template('donasikonten4.html')

def donasikonten5():
    return render_template('donasikonten5.html')

def donasikonten6():
    return render_template('donasikonten6.html')

def donasikonten7():
    return render_template('donasikonten7.html')

def donasikonten8():
    return render_template('donasikonten8.html')

def donasikonten9():
    return render_template('donasikonten9.html')
def get_profil():
    user = get_user_by_email(session.get('email'))
    return render_template('profil.html', profil=user)

def daftar():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        no_tlp=request.form['no_tlp']
        password = request.form['password']

        
        create_user(fullname, email, password,no_tlp)
        return redirect(url_for('login'))

    return render_template('daftar.html')

def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Fetch the user from the database using the provided email
        user = get_user_by_email(email)

        if user:
            stored_password = user[6]  # Assume the password is stored in user[2]
            
            # Check if the password matches
            if verify_password(user[6], password):
                session['user_id'] = user[0]
                session['fullname'] = user[1]
                session['email'] = user[3]

                flash('Login successful!', 'success')
                return redirect(url_for('beranda'))
            else:
                flash(f'Incorrect password. Please try again.{verify_password(stored_password, password), stored_password, password}', 'error')
        else:
            flash('Email not found. Please register or try again.', 'error')
    
    return render_template('login.html')

def donasikonten1():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten1.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten1.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten1.html')

def donasikonten2():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten2.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten2.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten3.html')

def donasikonten3():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten3.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten3.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten3.html')

def donasikonten4():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten4.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten4.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten4.html')


def donasikonten5():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten5.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten5.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten5.html')



def donasikonten6():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten6.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten6.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten6.html')


def donasikonten7():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten7.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten7.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten7.html')

def donasikonten8():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten8.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten8.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten8.html')

def donasikonten9():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nominal = request.form.get('button')  
        if not nominal: 
            nominal = request.form.get('nominal')
        
        if nominal:  
            try:
                nominal = int(nominal)  
            except ValueError:

                return render_template('donasikonten9.html', error="Nominal tidak valid.")
        else:

            return render_template('donasikonten9.html', error="Mohon pilih nominal atau masukkan nominal lainnya.")

        nama = request.form.get('donorName', '')  
        pesan = request.form.get('donorMessage', '')  
        user_id=session['user_id']

   
        tambah_donasi(nominal, nama, pesan,user_id)


        return redirect(url_for('profil'))

    return render_template('donasikonten9.html')

    
def akun():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    
    # Memanggil fungsi get_user_pekerjaan untuk mendapatkan data pekerjaan yang didaftar
    donasi = get_user_donasi(user_id)
    
    return render_template('profil.html', fullname=session['fullname'],email=session['email'], donasi=donasi ,no_hp=session['no_hp'])
    

def logout():
    session.pop('user_id', None)
    session.pop('fullname', None)
    # session.pop['email',None]
    # session.pop['no_hp',None]

    # flash('Anda telah logout.', 'info')
    return redirect(url_for('beranda'))
