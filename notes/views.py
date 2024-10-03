from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note
from products.models import Product
from .forms import NoteForm

# View to list all notes for a specific product
@login_required
def note_list(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    notes = Note.objects.filter(product=product, user=request.user)
    return render(request, 'notes/note_list.html', {'product': product, 'notes': notes})

# View to add a new note
@login_required
def add_note(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.product = product
            note.save()
            messages.success(request, 'Note added successfully!')
            return redirect('note_list', product_id=product.id)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'product': product})

# View to edit an existing note
@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('note_list', product_id=note.product.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'note': note})

# View to delete a note
@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    product_id = note.product.id
    note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('note_list', product_id=product_id)
