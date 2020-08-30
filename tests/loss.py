# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unittests for functional.loss."""

import unittest

import jax.numpy as jn

import objax


class TestLoss(unittest.TestCase):
    def test_on_mae(self):
        """Test mean absolute error on x and y."""
        x = jn.array([[0.76, 0.38, 0.51, 0.59], [0.89, 0.76, 0.17, 0.19], [0.14, 0.29, 0.49, 0.55]])
        y = jn.array([[1, 0, 4, 3], [4, 0, 4, 3], [0, 0, 0, 2]], dtype=jn.uint32)
        e = objax.functional.loss.mean_absolute_error(x, y)
        gold = jn.array([1.6300001, 2.6275, 0.59250003])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_mae_keep_dims(self):
        """Test mean absolute error on x and y with keep_dims."""
        x = jn.array([[0.76, 0.38, 0.51, 0.59], [0.89, 0.76, 0.17, 0.19], [0.14, 0.29, 0.49, 0.55]])
        y = jn.array([[1, 0, 4, 3], [4, 0, 4, 3], [0, 0, 0, 2]], dtype=jn.uint32)
        e = objax.functional.loss.mean_absolute_error(x, y, [1])
        gold = jn.array([1.1633334 , 0.47666666, 2.6033332 , 2.2233334 ])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_mae_no_dims(self):
        """Test mean absolute error on x and y with no keep_dims."""
        x = jn.array([[0.76, 0.38, 0.51, 0.59], [0.89, 0.76, 0.17, 0.19], [0.14, 0.29, 0.49, 0.55]])
        y = jn.array([[1, 0, 4, 3], [4, 0, 4, 3], [0, 0, 0, 2]], dtype=jn.uint32)
        e = objax.functional.loss.mean_absolute_error(x, y, [])
        gold = jn.array(1.6166668)
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_mse(self):
        """Test mean squared error on x and y."""
        x = jn.array([[0.76, 0.38, 0.51, 0.59], [0.89, 0.76, 0.17, 0.19], [0.14, 0.29, 0.49, 0.55]])
        y = jn.array([[1, 0, 4, 3], [4, 0, 4, 3], [0, 0, 0, 2]], dtype=jn.uint32)
        e = objax.functional.loss.mean_squared_error(x, y)
        gold = jn.array([4.54755, 8.203675, 0.61157507])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_mse_keep_dims(self):
        """Test mean squared error on x and y with keep_dims."""
        x = jn.array([[0.76, 0.38, 0.51, 0.59], [0.89, 0.76, 0.17, 0.19], [0.14, 0.29, 0.49, 0.55]])
        y = jn.array([[1, 0, 4, 3], [4, 0, 4, 3], [0, 0, 0, 2]], dtype=jn.uint32)
        e = objax.functional.loss.mean_squared_error(x, y, [1])
        gold = jn.array([3.249767, 0.2687, 9.0297, 5.2689])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_mse_no_dims(self):
        """Test mean squared error on x and y with no keep_dims."""
        x = jn.array([[0.76, 0.38, 0.51, 0.59], [0.89, 0.76, 0.17, 0.19], [0.14, 0.29, 0.49, 0.55]])
        y = jn.array([[1, 0, 4, 3], [4, 0, 4, 3], [0, 0, 0, 2]], dtype=jn.uint32)
        e = objax.functional.loss.mean_squared_error(x, y, [])
        gold = jn.array(4.454267)
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_mean_squared_log_error(self):
        """Test mean squared error on x and y."""
        x = jn.array([3, 5, 2, 7], dtype=jn.float32)
        y = jn.array([2, 5, 4, 8], dtype=jn.float32)
        output = objax.functional.loss.mean_squared_log_error(x, y)
        expected = jn.array([0.08276097, 0., 0.26094282, 0.013872852], dtype=jn.float32)
        self.assertAlmostEqual(jn.abs(output - expected).sum(), 0, delta=1e-12)

    def test_on_mean_squared_log_error_keep_dims(self):
        """Test mean squared error on x and y with keep_dims."""
        x = jn.array([[3, 5, 2.5, 7]], dtype=jn.float32)
        y = jn.array([[2.5, 5, 4, 8]], dtype=jn.float32)
        output = objax.functional.loss.mean_squared_log_error(x, y, keep_dims=(0,))
        expected = jn.array([0.039730113], dtype=jn.float32)
        self.assertAlmostEqual(jn.abs(output - expected).sum(), 0, delta=1e-12)

    def test_on_mean_squared_log_error_no_dims(self):
        """Test mean squared error on x and y with no keep_dims."""
        x = jn.array([[0.1152, 0.6301, 0.6845], [0.0958, 0.2180, 0.8503]], dtype=jn.float32)
        y = jn.array([[0.0026, 0.9501, 0.1955], [0.3537, 0.1689, 0.7774]], dtype=jn.float32)
        output = objax.functional.loss.mean_squared_log_error(x, y, keep_dims=())
        expected = jn.array(0.03483658, dtype=jn.float32)
        self.assertAlmostEqual(jn.abs(output - expected).sum(), 0, delta=1e-12)

    def test_on_xe_logits_2d(self):
        """Test cross-entropy on logits."""
        x = jn.array([[0.58, 0.4, 0.02], [0.36, 0.27, 0.37], [0.46, 0.24, 0.3], [0.35, 0.29, 0.36]])
        e = objax.functional.loss.cross_entropy_logits(10 * x, x)
        gold = jn.array([0.9881458, 1.126976, 1.2800856, 1.1140614])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_xe_logits_2d_broadcast(self):
        """Test cross-entropy on logits, broadcasted labels."""
        x = jn.array([[0.58, 0.4, 0.02], [0.36, 0.27, 0.37], [0.46, 0.24, 0.3], [0.35, 0.29, 0.36]])
        e = objax.functional.loss.cross_entropy_logits(10 * x, x[:1])
        gold = jn.array([0.9881458, 1.278976, 1.1840856, 1.2140613])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_xe_logits_5d(self):
        """Test cross-entropy on logits in 5d."""
        x = jn.array([[0.58, 0.4, 0.02], [0.36, 0.27, 0.37], [0.46, 0.24, 0.3], [0.35, 0.29, 0.36]])
        x = x.reshape((2, 1, 1, 2, 3))
        e = objax.functional.loss.cross_entropy_logits(10 * x, x)
        gold = jn.array([0.9881458, 1.126976, 1.2800856, 1.1140614]).reshape((2, 1, 1, 2))
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_xe_logits_5d_broadcast(self):
        """Test cross-entropy on logits in 5d, broadcasted labels."""
        x = jn.array([[0.58, 0.4, 0.02], [0.36, 0.27, 0.37], [0.46, 0.24, 0.3], [0.35, 0.29, 0.36]])
        x = x.reshape((2, 1, 1, 2, 3))
        e = objax.functional.loss.cross_entropy_logits(10 * x, x[:1])
        gold = jn.array([[[[0.9881458, 1.126976]]], [[[1.1840856, 1.1010613]]]])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)
        e = objax.functional.loss.cross_entropy_logits(10 * x, x[:, :, :, :1])
        gold = jn.array([[[[0.9881458, 1.278976]]], [[[1.2800856, 1.0900612]]]])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)

    def test_on_xe_logits_sparse(self):
        """Test cross-entropy on logits with sparse labels."""
        x = jn.array([[0.58, 0.4, 0.02], [0.36, 0.27, 0.37], [0.46, 0.24, 0.3], [0.35, 0.29, 0.36]])
        y = jn.array([0, 1, 2, 1], dtype=jn.uint32)
        e = objax.functional.loss.cross_entropy_logits_sparse(10 * x, y)
        gold = jn.array([0.15614605, 1.820976, 1.8720856, 1.5760615])
        self.assertAlmostEqual(jn.abs(e - gold).sum(), 0, delta=1e-12)


if __name__ == '__main__':
    unittest.main()
