"""
==========================================
Basis module (:mod:`quspin.basis`)
==========================================

Basis classes for quantum many-body systems.

The following table shows the available operator strings for the different bases (`sps` is the onsite Hilbert space dimension):

.. math::
   \\begin{array}{cccc}
      \\texttt{basis}/\\texttt{opstr}   &   \\texttt{"I"}   &   \\texttt{"+"}   &   \\texttt{"-"}  &   \\texttt{"n"}   &   \\texttt{"z"}   &   \\texttt{"x"}   &   \\texttt{"y"}  \\newline  
      \\texttt{spin_basis_*} &   \\hat{1}        &   \\hat S^+(\\hat\\sigma^+)       &   \\hat S^-(\\hat\\sigma^-)      &         -         &   \\hat S^z(\\hat\\sigma^z)       &   \\hat S^x(\\hat\\sigma^x)     &   \\hat S^y(\\hat\\sigma^y)  \\  \\newline
      \\texttt{boson_basis_*}&   \\hat{1}        &   \\hat b^\\dagger      &       \\hat b          & \\hat b^\\dagger \\hat b     &  \\hat b^\\dagger\\hat b - \\frac{\\mathrm{sps}-1}{2}       &   -       &   -  \\newline
      \\texttt{*_fermion_basis_*}& \\hat{1}        &   \\hat c^\\dagger      &       \\hat c          & \\hat c^\\dagger \\hat c     &  \\hat c^\\dagger\\hat c - \\frac{1}{2}       &   -       &   -  \\newline
   \\end{array}

**Note:** The default operators for spin-1/2 are the Pauli matrices, NOT the spin operators. To change this, see
the argument `pauli` of the `spin_basis_*` classes. Higher spins can only be defined using the spin operators, and do NOT support
the operator strings "x" and "y". 

.. currentmodule:: quspin.basis

one-dimensional symmetries
---------------------------

.. autosummary::
   :toctree: generated/

   spin_basis_1d
   boson_basis_1d
   spinless_fermion_basis_1d
   spinful_fermion_basis_1d

general lattice symmetries
-----------------------------

.. autosummary::
   :toctree: generated/

   spin_basis_general
   boson_basis_general
   spinless_fermion_basis_general
   spinful_fermion_basis_general


combining basis classes
-----------------------

.. autosummary::
   :toctree: generated/

   tensor_basis
   photon_basis

functions
----------

.. autosummary::
   :toctree: generated/

   coherent_state
   photon_Hspace_dim

large integer support
=====================

QuSpin defined dtype
--------------------

.. autosummary::
   :toctree: generated/

   uint256
   uint1024
   uint4096
   uint16384

Array initialization routines
-----------------------------

.. autosummary::
   :toctree: generated/

   basis_ones
   basis_zeros





Utilities to use large integers
-------------------------------

.. autosummary::
   :toctree: generated/
  
   get_basis_type
   bitwise_not
   bitwise_and
   bitwise_or
   bitwise_xor
   bitwise_left_shift
   bitwise_right_shift


"""
from .basis_1d import *
from .basis_general import *
from .base import *
from .lattice import *
from .photon import *
from .tensor import *
from ._basis_utils import *
