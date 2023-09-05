#!/usr/bin/python3
"""Checks if a matrix multiplication function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """A function that Multiplies two matrices.
    Args:
        m_a : 1st matrix.
        m_b : 2nd matrix.
    """
    
    return (np.matmul(m_a, m_b))
